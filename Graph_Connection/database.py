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

    @staticmethod
    def insert_objects(tx, creator):
        creation = ""
        result = tx.run(creation)
        return result
