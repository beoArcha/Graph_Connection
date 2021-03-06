from neo4j import GraphDatabase


class Database(object):
    """Manage connection to neo4j"""

    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._driver.close()

    def execute(self, func, *args):
        with self._driver.session() as session:
            return session.write_transaction(func, *args)

    @staticmethod
    def lookup(tx, m=10):
        result = tx.run("MATCH (n) RETURN n LIMIT {}".format(m))
        return result

    @staticmethod
    def delete_all(tx):
        result = tx.run("MATCH (n) OPTIONAL MATCH (n)-[r]-() DELETE n, r;")
        return result

    def insert_objects(self, creator):
        with self._driver.session() as session:
            tx = session.begin_transaction()
            info = dict()
            for creator_item in creator:
                node_id = self.create_node(tx, creator_item)
                info[creator_item.id_number] = node_id
                creator_item.node_id = node_id
            tx.commit()
            tx = session.begin_transaction()
            for creator_item in creator:
                self.create_edge(tx, creator_item)
            tx.commit()

    @staticmethod
    def create_node(tx, creator_item):
        params_str = ""
        for p in range(0, len(creator_item.params)):
            params_str = "{} {}:{},".format(params_str, str(creator_item.columns[p]), str(creator_item.params[p]))
        params_str = "{} id:{}".format(params_str, str(creator_item.id_number))
        txt = "CREATE (id_{id_number}:`{class_number}` {{{params}}}) RETURN id(id_{id_number})".format(
            id_number=creator_item.id_number,
            class_number=creator_item.class_con,
            params=params_str)
        # print(txt)
        return tx.run(txt).single().value()

    @staticmethod
    def create_edge(tx, creator_item):
        for e, neighbour in enumerate(creator_item.neighbours):
            if neighbour != creator_item.id_number:
                txt = "MATCH (i{{id:{id_number}}}), (j{{id:{neighbour}}})" \
                      "CREATE ((i)-[:neighbour{{distance:{distance}}}]->(j));".format(
                    id_number=creator_item.id_number,
                    neighbour=neighbour,
                    distance=creator_item.distances[e]
                )
                tx.run(txt)
                # print(txt)

    @staticmethod
    def get_path(tx, start, end):
        txt = "MATCH (start{{id:{start}}}), (end{{id:{end}}}) " \
              "CALL algo.shortestPath.stream(start, end, \"distance\") " \
              "YIELD nodeId, cost " \
              "MATCH (other) WHERE id(other) = nodeId " \
              "RETURN other.id AS name, cost".format(
            start=start,
            end=end
        )
        result = tx.run(txt)
        return result

    @staticmethod
    def get_closeness(tx, target_class, is_huge=False):
        txt = "CALL  algo.closeness.stream('{target_class}', 'neighbour'{huge})" \
              "YIELD nodeId, centrality " \
              "RETURN algo.asNode(nodeId).id " \
              "AS node, centrality ORDER BY centrality DESC ".format(
            target_class=target_class,
            huge=", {graph:'huge'} " if is_huge else " "
        )
        result = tx.run(txt)
        return result

    @staticmethod
    def get_eigenvector(tx, target_class):
        txt = "CALL algo.eigenvector.stream('{target_class}', 'neighbour') " \
              "YIELD nodeId, score " \
              "RETURN algo.asNode(nodeId).id AS page, score " \
              "ORDER BY score DESC".format(
            target_class=target_class
        )
        result = tx.run(txt)
        return result

    @staticmethod
    def get_degree_centrality(tx):
        txt = "MATCH (n) RETURN n.id AS name, size(()-[:neighbour]->(n)) AS degree ORDER BY degree DESC"
        result = tx.run(txt)
        return result

    @staticmethod
    def get_betweenness(tx, target_class):
        txt = "CALL algo.betweenness.stream('{target_class}', 'neighbour', {{direction:'out'}}) " \
                "YIELD nodeId, centrality " \
                "MATCH (n:`1`) WHERE id(n) = nodeId " \
                "RETURN n.id AS n,centrality " \
                "ORDER BY centrality DESC".format(
                 target_class=target_class
        )
        result = tx.run(txt)
        return result
