from neo4j import GraphDatabase


class Database(object):

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
            # tx = session.begin_transaction()
            # for creator_item in creator:
            #   self.create_edge(tx, creator_item)
            # tx.commit()

    @staticmethod
    def create_node(tx, creator_item):
        params_str = ""
        for p in range(0, len(creator_item.params)):
            params_str = "{} {}:{},".format(params_str, str(creator_item.columns[p]), str(creator_item.params[p]))
        params_str = params_str[0:len(params_str) - 1]
        return tx.run("CREATE (`{id_number}`:`{class_number}` {{{params}}}) RETURN id(`{id_number}`)".format(
            id_number=creator_item.id_number,
            class_number=creator_item.class_con,
            params=params_str)).single().value()

    @staticmethod
    def create_edge(tx, creator_item):
        tx.run("MATCH (a:Person) WHERE id(a) = $id ")
