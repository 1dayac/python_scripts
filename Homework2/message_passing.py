__author__ = 'dima'



class Vertex(object):
    def __init__(self, id, type):
        self.__id = id
        self.__type = type

    def getId(self):
        return self.__id

    def getType(self):
        return self.__type


class FactorGraph(object):
    def __init__(self):
        self.__graph_dict = {}

    def add_vertex(self, vertex):
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]
        if vertex2 in self.__graph_dict:
            self.__graph_dict[vertex2].append(vertex1)
        else:
            self.__graph_dict[vertex2] = [vertex1]



