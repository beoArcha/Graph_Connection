#!/usr/bin/python3
from Graph_Connection.creator import Creator
from Graph_Connection.data_import import DataImport
from Graph_Connection.database import Database
from Graph_Connection.networking import Networking
from os import path
import argparse


def main(**kwargs) -> None:
    # region args_parser
    args = parsing_args()
    if args.default is not None or args.default == 0:
        full_address, target_class, separator, index, name = preset_data(args.default)
    else:
        full_address = args.address
        target_class = args.target_class
        separator = args.separator
        index = args.index
    name = args.name
    neighbors_number = args.neighbors
    debug_mode = args.debug
    # endregion
    # region source
    data_source = DataImport(full_address, target_class, separator, index)
    data_source.eliminate_nan()
    data_source.normalize()
    data_source.split()
    index = data_source.return_index()
    np_train, class_train, np_full, class_full = data_source.return_all()
    neighbors = Networking(np_train)
    neighbors.k_neighbors()
    neighbors_list = neighbors.neighbors()
    distances = neighbors.distances
    # endregion
    creator = Creator(neighbors_list, np_train, data_source.columns,
                      index, target_class, distances, class_train).list_of_objects
    # region connection
    connection_database = None
    try:
        connection_database = Database(args.uri, args.user, args.password)
        answer = connection_database.execute(connection_database.lookup, 25)
        if answer is not None and len(answer.values()) > 0:
            answer = connection_database.execute(connection_database.delete_all)
            print("Database cleaned\n{}".format(answer))
        answer = connection_database.execute(connection_database.insert_objects(creator))
    finally:
        connection_database.close()
    # endregion


def parsing_args() -> argparse:
    """Prepare starting arguments"""
    parser = argparse.ArgumentParser(description="Build networked data source for neo4js database.")
    parser.add_argument("--address", "-a", help="File address", type=str)
    parser.add_argument("--neighbors", "-n", help="Number of neighbors", type=int, default=5)
    parser.add_argument("--separator", "-s", help="CSV file separator", type=str, default=",")
    parser.add_argument("--target_class", "-c", help="Target class", type=str, default="class")
    parser.add_argument("--uri", "-ur", help="Address", type=str, default="bolt://localhost:7687")
    parser.add_argument("--user", "-us", help="User", type=str, default="neo4j")
    parser.add_argument("--password", "-pass", help="Password", type=str, default="noSQL")
    parser.add_argument("--name", "-na", help="Name", type=str)
    parser.add_argument("--index", "-i", help="Is index", action="store_true")
    parser.add_argument("--default", "-d", help="Default set", type=int, default=0)
    parser.add_argument("--debug", "-de", help="Debug mode", action="store_true")
    return parser.parse_args()


def preset_data(num: int) -> tuple:
    sep = ";"
    index = 0
    if num == 1:
        full = r"{}\Data\blood.csv"
        target = "class"
        index = False
        name = "Blood"
    elif num == 2:
        full = r"{}\Data\BreastTissue.csv"
        target = "Class"
        index = 0
        name = "BreastTissue"
    elif num == 3:
        full = r"{}\Data\Cryotherapy.csv"
        target = "Result_of_Treatment"
        index = False
        name = "Cryotherapy"
    elif num == 4:
        full = r"{}\Data\Health.CSV"
        target = "REZULTAT"
        name = "Health"
    elif num == 5:
        full = r"{}\Data\heart_swiss.csv"
        target = "num"
        index = False
        name = "Heart"
    elif num == 6:
        full = r"{}\Data\ILPD.csv"
        target = "Selector"
        index = False
        name = "ILPD"
    elif num == 7:
        full = r"{}\Data\iris.csv"
        target = "class"
        name = "Iris"
    elif num == 8:
        full = r"{}\Data\Knowledge.csv"
        target = "UNS"
        index = False
        name = "Knowledge"
    elif num == 9:
        full = r"{}\Data\magic.csv"
        target = "class"
        index = False
        name = "MAGIC"
    elif num == 10:
        full = r"{}\Data\Mammographic.csv"
        target = "Severity"
        index = False
        name = "Mammographic"
    elif num == 11:
        index = False
        full = r"{}\Data\Contraceptive.csv"
        target = "Contraceptive"
        name = "Contraceptive"
    elif num == 12:
        full = r"{}\Data\voting.csv"
        target = "class"
        index = False
        name = "Voting"
    elif num == 13:
        full = r"{}\Data\Wine.CSV"
        target = "class"
        name = "Wine"
    elif num == 14:
        full = r"{}\Data\wine_quality.csv"
        target = "quality"
        index = False
        name = "Wine_Quality"
    elif num == 15:
        full = r"{}\Data\yeast.csv"
        target = "class"
        name = "Yeast"
    else:
        full, target, sep, index, name = preset_data(7)
    directory = path.split(path.dirname(__file__))
    return full.format(directory[0]), target, sep, index, name


if __name__ == "__main__":
    main()
