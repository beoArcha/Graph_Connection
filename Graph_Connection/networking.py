from sklearn.neighbors import NearestNeighbors


class Networking:
    """Class creating network from Numpy matrix"""
    def __init__(self, np_data, number_of_neighbors=5, algorithm="auto"):
        self.nbrs = NearestNeighbors(n_neighbors=number_of_neighbors, algorithm=algorithm).fit(np_data)
        self.np_data = np_data
        self.number_of_neighbors = number_of_neighbors
        self.distances = ""
        self.indices = ""

    def k_neighbors(self):
        self.distances, self.indices = self.nbrs.kneighbors(self.np_data)

    def neighbors(self, mode_type="distance"):
        return self.nbrs.kneighbors_graph(self.np_data, self.number_of_neighbors, mode=mode_type)
