import math
# --------------------------------------------------------------------------------------
class Vertex:

    def __init__(self, name):
        self.__edgesIn = []
        self.__edgesOut = []
        self.__name = name
        self.__distance = math.inf
        self.__color = ''
        self.__father = None
    
    def getName(self):
        return self.__name

    def getEdge(self):
        return self.__edgesOut
    
    def removeEdge(self, name):
        index = 0
        for edge in self.__edgesOut:
            if name == edge.getName():
                del(self.__edgesOut[index])
            index+=1

    def printVertexName(self):
        print("|", self.__name, "|", end = "")

    def printAllEdge(self):
        for edge in self.__edgesOut:
            print(" --> ", end = "")
            edge.printVertexName()

        print(" --> NULL")

    def existEdge(self, name):
        count = 0
        for edge in self.__edgesOut:
            if edge.getName() == name:
                count+=1
        return count

    def getOrdemEdge(self):
        return len(self.__edgesOut)

    def setColor(self, color):
        self.__color = color

    def setDistance(self, distance):
        self.__distance = distance

    def setFather(self, father):
        self.__father = father
    
    def getDistance(self):
        return self.__distance

    def getColor(self):
        return self.__color

# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------            
class Grafo:
    
    def __init__(self):
        self.__vertex = []
        self.__digrafo = True
        self.__q = []

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

    def widthSearch(self, vertex):
        for v in self.__vertex:
            v.setColor('branco')
            v.setDistance(math.inf)
            v.setFather(None)
        vertex.setColor('cinza')
        vertex.setDistance(0)
        vertex.setFather(None)
        self.__q.append(vertex)

        while len(self.__q) != 0:
            used = self.__q.pop()
            for ver in used.getEdge():
                if ver.getColor() == 'branco':
                    ver.setColor('cinza')
                    ver.setDistance(used.getDistance()+1)
                    ver.setFather(used)
                    self.__q.append(ver)
            used.setColor('preto')



# --------------------------------------------------------------------------------------

# gg = Grafo()

# gg.addVertex("1")
# gg.addVertex("2")
# gg.addVertex("3")
# gg.addVertex("4")
# gg.addVertex("5")

# gg.addEdge("1", "2")
# gg.addEdge("1", "3")
# gg.addEdge("3", "2")
# gg.addEdge("1", "2")
# gg.addEdge("2", "4")
# gg.addEdge("4", "2")
# gg.addEdge("3", "5")

# print("------------------------------------------")
# gg.printAll()

# # gg.removeVertex("2")
# print(gg.getOrdem("1"))
# print("------------------------------------------")
# gg.printAll()

# print("------------------------------------------")