
class Vertex:
    self.__name = ""
    self.__edges = []

    def __init__(self, name):
        self.__name = name
    
    def getName(self):
        return self.__name

    def getEdge(self):
        return self.__edges

class Grafo:
    self.__list = []
    self.__digrafo = True

    def __init__(self):
        pass

    def addVert(self, name):
        self.__list.append(Vertex(name))
    

    def getVertex(self, name):
        for vertex in self.__list:
            if vertex.getName() == name:
                return vertex
        return None


    def addEdge(self, vertInit, vertEnd):
        vInit = self.getVertex(vertInit)

        if vInit == None:
            print("ALERT: Vertex" + vertInit + "undefined")
            return None

        vEnd = self.getVertex(vertEnd)

        if vEnd == None:
            print("ALERT: Vertex" + vertEnd + "undefined")
            return None

        vInit.getEdge().append(vEnd)
        print("Sucess")
        return 1

