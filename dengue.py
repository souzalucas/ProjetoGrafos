import Grafo


# grafo = Grafo.Grafo()
































gg = Grafo.Grafo(True)

gg.addVertex("1")
gg.addVertex("2")
gg.addVertex("3")
gg.addVertex("4")
gg.addVertex("5")
gg.addVertex("6")
gg.addVertex("7")

gg.addEdge("1", "3")
gg.addEdge("2", "3")
gg.addEdge("3", "4")
gg.addEdge("4", "5")
gg.addEdge("5", "6")
gg.addEdge("5", "7")

print("------------------------------------------")
gg.printAll()

print("------------------------------------------")

print(gg.getMinMaxDistance())
print("------------------------------------------")