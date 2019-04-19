import Grafo

import sys

text = open(sys.argv[1], 'r')

lines = text.read().split('\n')
vertex = []
vQtd = int(lines[0])

index = 1
teste = 1
while vQtd != 0:
  gg = Grafo.Grafo(True)
  #print(vQtd)
  for i in range(vQtd - 1):
    gg.addVertex(lines[index].split(' ')[0])
    gg.addVertex(lines[index].split(' ')[1])
    gg.addEdge(lines[index].split(' ')[0], lines[index].split(' ')[1])
    index += 1
  
  if vQtd == 1:
    index += 1

  print('Teste', teste)
  vert = 1 if (vQtd == 1) else gg.getMinMaxDistance()
  print(vert, '\n')
  vQtd = int(lines[index])
  index += 1
  teste += 1
