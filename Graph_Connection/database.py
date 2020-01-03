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
    def get_path(txt, start, end):
        pass

    @staticmethod
    def get_between(txt):
        pass
