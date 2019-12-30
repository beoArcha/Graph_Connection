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

    def return_all(self):
        return self.X_train, self.Y_train, self.X_test, self.Y_test

    def return_index(self):
        return range(0, len(self.X_train))
