from .data_import import DataImport
import argparse


def main(**kwargs) -> None:
    full_address, target_class, separator, index = preset_data(9)
    data_source = DataImport(full_address, target_class, separator, index)
    data_source.eliminate_nan()
    data_source.normalize()
    x_train, x_test, y_train, y_test, number_of_sets = data_source.multi_split()


def parsing_args() -> argparse:
    """Prepare starting arguments"""
    parser = argparse.ArgumentParser(description="Build networked data source fro neo4js database.")
    parser.add_argument("--address", "-a", help="File address", type=str)
    parser.add_argument("--separator", "-s", help="CSV file separator", type=str, default=",")
    parser.add_argument("--class", "-c", help="Target class", type=str, default=",")
    parser.add_argument("--index", "-i", help="Is index", action="store_true")
    parser.add_argument("--debug", "-de", help="Debug mode", action="store_true")
    return parser.parse_args()


def preset_data(a):
    return 0, 0, 0


if __name__ == "__main__":
    main()
