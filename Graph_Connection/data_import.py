import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split


class DataImport:
    """Class importing csv file and returning Numpy matrix"""
    def __init__(self, full_address, target_class, separator=";", index=0):
        data_frame_full = pd.read_csv(full_address, index_col=index, sep=separator)
        self.data_frame = data_frame_full.drop(columns=target_class)
        self.index = self.data_frame.index
        self.series_target = data_frame_full[target_class]
        self.target = target_class
        self.scaler = MinMaxScaler()
        self.X_test = ""
        self.Y_test = ""
        self.X_train = ""
        self.Y_train = ""

    def eliminate_nan(self):
        self.data_frame = self.data_frame.fillna(0)

    def eliminate_nan_mean(self):
        self.data_frame = self.data_frame.fillna(self.data_frame.mean())

    def normalize(self):
        self.scaler.fit(self.data_frame)
        self.data_frame = self.scaler.transform(self.data_frame)

    def split(self):
        np_array_temp = self.series_target.tolist()
        self.X_train, self.X_test, self.Y_train, self.Y_test = train_test_split(self.data_frame,
                                                                                np_array_temp,
                                                                                test_size=0.5, random_state=101)

    def multi_split(self):
        print("*{}*".format("|" * 20))
        number_of_sets = 20
        x = self.data_frame
        y = self.series_target.tolist()
        d = dict()
        x_test = dict()
        x_train = dict()
        y_test = dict()
        y_train = dict()
        print("*{}*".format("|"*20))
        for i in range(0, number_of_sets):
            d[i] = int((len(y) / number_of_sets)) * i
        d[number_of_sets] = len(y)
        for i in range(0, number_of_sets):
            print("*{:^20}*".format("|" * (i + 1)))
            tx = list()
            ty = list()
            for j in range(0, d[i+1]):
                tx.append(x[j])
                ty.append(y[j])
            X_train, X_test, Y_train, Y_test = train_test_split(tx, ty, test_size=0.5, random_state=101)
            x_test[i] = X_test
            x_train[i] = X_train
            y_test[i] = Y_test
            y_train[i] = Y_train
        return x_train, x_test, y_train, y_test, number_of_sets

    def return_all(self):
        return self.X_train, self.Y_train, self.X_test, self.Y_test

    def return_index(self):
        return range(0, len(self.X_train))



