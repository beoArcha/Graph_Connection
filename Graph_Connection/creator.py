class CreatorItem(object):
    def __init__(self, neighbors, params, id_number, distances, columns, own_class):
        self.neighbours = neighbors
        self.params = params
        self.id = id_number
        self.distances = distances
        self.columns = columns
        self.class_con = own_class


class Creator:
    def __init__(self, neighbors, full, columns, index, target, distances, class_target):
        self.list_of_objects = self.creator_item(neighbors, full, columns, index, target, distances, class_target)

    @staticmethod
    def creator_item(neighbors, full, columns, index, target, distances, class_target):
        ret = list()
        all_cols = list()
        for c in columns:
            if c != target:
                all_cols.append(c)
        for i in index:
            own_neighbors = neighbors[i]
            own_params = full[i]
            own_distances = distances[i]
            own_class = class_target[i]
            ci = CreatorItem(own_neighbors, own_params, i, own_distances, all_cols, own_class)
            ret.append(ci)
        return ret
