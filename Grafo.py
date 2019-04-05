# --------------------------------------------------------------------------------------
class Vertex:

    def __init__(self, name):
        self.__edges = []
        self.__name = name
    
    def getName(self):
        return self.__name

    def getEdge(self):
        return self.__edges
    
    def removeEdge(self, name):
        index = 0
        for edge in self.__edges:
            if name == edge.getName():
                del(self.__edges[index])
            index+=1

    def printVertexName(self):
        print("|", self.__name, "|", end = "")

    def printAllEdge(self):
        for edge in self.__edges:
            print(" --> ", end = "")
            edge.printVertexName()

        print(" --> NULL")

    def existEdge(self, name):
        count = 0
        for edge in self.__edges:
            if edge.getName() == name:
                count+=1
        return count

    def getOrdemEdge(self):
        return len(self.__edges)

# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------            
class Grafo:
    
    def __init__(self):
        self.__vertex = []
        self.__digrafo = True

    def addVertex(self, name):
        self.__vertex.append(Vertex(name))
    

    def getVertex(self, name):
        for vertex in self.__vertex:
            if vertex.getName() == name:
                return vertex
        return None


    def addEdge(self, vertInit, vertEnd):
        vInit = self.getVertex(vertInit)

        if vInit == None:
            return None

        vEnd = self.getVertex(vertEnd)

        if vEnd == None:
            return None

        vInit.getEdge().append(vEnd)
        return 1

    def printAll(self):
        for vertex in self.__vertex:
            vertex.printVertexName()
            vertex.printAllEdge()

    def __removeVertex(self, name):
        index = 0
        for vertex in self.__vertex:
            if name == vertex.getName():
                del(self.__vertex[index])
            index+=1

    def removeVertex(self, name):
        for vertex in self.__vertex:
            vertex.removeEdge(name)
        self.__removeVertex(name)

    def removeEdge(self, vertIni, vertEnd):
        for vertex in self.__vertex:
            if vertIni == vertex.getName():
                vertex.removeEdge(vertEnd)
    
    def getOrdem(self, vert):
        ordem = 0
        for vertex in self.__vertex:
            if vert == vertex.getName():
               ordem += vertex.getOrdemEdge()
            else: 
                ordem += vertex.existEdge(vert)
        return ordem
# --------------------------------------------------------------------------------------

gg = Grafo()

gg.addVertex("1")
gg.addVertex("2")
gg.addVertex("3")
gg.addVertex("4")
gg.addVertex("5")

gg.addEdge("1", "2")
gg.addEdge("1", "3")
gg.addEdge("3", "2")
gg.addEdge("1", "2")
gg.addEdge("2", "4")
gg.addEdge("4", "2")
gg.addEdge("3", "5")

print("------------------------------------------")
gg.printAll()

# gg.removeVertex("2")
print(gg.getOrdem("1"))
print("------------------------------------------")
gg.printAll()

print("------------------------------------------")