import math
# --------------------------------------------------------------------------------------
class Vertex:

    def __init__(self, name, health, health_regen, base_armor, attack, attack_rate):
        self.__edgesIn = []
        self.__edgesOut = []
        self.__name = name
        self.__health = health
        self.__health_regen = health_regen
        self.__base_armor = base_armor
        self.__attack = attack
        self.__attack_rate = attack_rate
        self.__distance = - math.inf
        self.__color = ''
        self.__father = None
        self.__wins = 0
        self.__winsVet = []

    def __repr__(self):
        return self.__name

    def __str__(self):
        return self.__name
    
    def getName(self):
        return self.__name

    def getWin(self):
        return self.__wins
    
    def getWinsVet(self):
        return self.__winsVet

    def getHealth(self):
        return self.__health
    
    def getHealthRegen(self):
        return self.__health_regen

    def getBaseArmor(self):
        return self.__base_armor

    def getAttack(self):
        return self.__attack

    def getAttackRate(self):
        return self.__attack_rate

    def getEdgeOut(self):
        return self.__edgesOut
    
    def getEdgeIn(self):
        return self.__edgesIn
    
    def getEdge(self):
        edge = self.__edgesOut + self.__edgesIn
        return edge

    def win(self):
        self.__wins += 1

    def appendWinsVet(self, vertex):
        self.__winsVet.append(vertex)
        
    def removeEdge(self, name):
        index = 0
        for edge in self.__edgesOut:
            if name == edge.getName():
                edge.removeEdgeIn(self)
                del(self.__edgesOut[index])
            index+=1

    def removeEdgeIn(self, edgeIn):
        index = 0
        for edge in self.__edgesIn:
            if edgeIn == edge:
                del(self.__edgesIn[index])
            index+=1

    def printVertexName(self):
        print("|", self.__name, "|", end = "")

    def printAllEdge(self):
        for edge in self.__edgesOut:
            print(" --> ", end = "")
            edge.printVertexName()

        print(" --> NULL")

    def getOrdemIn(self):
        return len(self.__edgesIn)

    def getOrdemOut(self):
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
    
    def __init__(self, digrafo):
        self.__vertex = []
        self.__digrafo = digrafo
        self.__q = []
    
    def addVertex(self, name, health, health_regen, base_armor, attack, attack_rate):
        if self.getVertex(name) == None:
            self.__vertex.append(Vertex(name, health, health_regen, base_armor, attack, attack_rate))
    

    def getVertex(self, name):
        for vertex in self.__vertex:
            if vertex.getName() == name:
                return vertex
        return None

    def getVertexList(self):
        return self.__vertex

    def addEdge(self, vertInit, vertEnd):
        vInit = self.getVertex(vertInit)

        if vInit == None:
            return None

        vEnd = self.getVertex(vertEnd)

        if vEnd == None:
            return None

        vInit.getEdgeOut().append(vEnd)
        vEnd.getEdgeIn().append(vInit)
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
                ordem += vertex.getOrdemOut()
                ordem += vertex.getOrdemIn()
        return ordem

    def widthSearch(self, vertex):
        for v in self.__vertex:
            v.setColor('white')
            v.setDistance(- math.inf)
            v.setFather(None)
        vertex.setColor('grey')
        vertex.setDistance(0)
        vertex.setFather(None)
        self.__q.append(vertex)

        while len(self.__q) != 0:
            used = self.__q.pop()
            for ver in used.getEdge():
                if ver.getColor() == 'white':
                    ver.setColor('grey')
                    ver.setDistance(used.getDistance()+1)
                    ver.setFather(used)
                    self.__q.append(ver)
            used.setColor('black')

    def getMinMaxDistance(self):
        minMax = math.inf
        vertMinMax = None
        for v in self.__vertex:
            self.widthSearch(v)
            maxDistance = - math.inf
            for ver in self.__vertex:
                dist = ver.getDistance()
                if dist > maxDistance:
                    maxDistance = dist
            if maxDistance < minMax:
                minMax = maxDistance
                vertMinMax = v
        return vertMinMax.getName()

    def isConnected(self):
        v = self.__vertex[0]
        self.widthSearch(v)
        for vert in self.__vertex:
            if (vert.getColor() != 'black'):
                return False
        return True

# --------------------------------------------------------------------------------------