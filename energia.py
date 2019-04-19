import Grafo

import sys

text = open(sys.argv[1], 'r')

lines = text.read().split('\n')
vertex = []
vQtd = int(lines[0].split(' ')[0])
eQtd = int(lines[0].split(' ')[1])
index = 1
test = 1
while (eQtd != 0 and vQtd != 0):
  gg = Grafo.Grafo(True)
  if (eQtd >= (vQtd -1)):
    for i in range(eQtd):
      if (i < vQtd):
        gg.addVertex(str(i+1))
      v1 = lines[index].split(' ')[0]
      v2 = lines[index].split(' ')[1]
      gg.addVertex(v1)
      gg.addVertex(v2)
      gg.addEdge(v1, v2)
      index += 1

    print('Teste', test)
    print(gg.isConnected())
    print('')
  else:
    index += eQtd + 1
    print('Teste', test)
    print('False\n')

  vQtd = int(lines[index].split(' ')[0])
  eQtd = int(lines[index].split(' ')[1])
  index += 1
  test += 1
