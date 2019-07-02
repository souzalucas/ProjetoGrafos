import sys
import Grafo
import requests

gg = Grafo.Grafo(True)

URL = "https://api.opendota.com/api/heroStats"

r = requests.get(url = URL) 
  
data = r.json()

for pers in data:
  gg.addVertex(pers["localized_name"], pers["base_health"], pers["base_health_regen"], pers["base_armor"], pers["base_attack_min"], pers["attack_rate"])
# print("--------------------------Antes--------------------------")
# gg.printAll()
# print("--------------------------Antes--------------------------")

for vertexOut in gg.getVertexList():
  for vertexIn in gg.getVertexList():
    gg.addEdge(vertexOut.getName(), vertexIn.getName())


for challenger in gg.getVertexList():
  for challenged in challenger.getEdgeOut():
    if(challenger.getName() != challenged.getName()):
      challengerHealth = challenger.getHealth()
      challengedHealth = challenged.getHealth()

      challengerHealthRegen = challenger.getHealthRegen()
      challengedHealthRegen = challenged.getHealthRegen()

      challengerBaseArmor = challenger.getBaseArmor()
      challengedBaseArmor = challenged.getBaseArmor()

      challengerAttack = challenger.getAttack()
      challengedAttack = challenged.getAttack()

      challengerAttackRate = challenger.getAttackRate()
      challengedAttackRate = challenged.getAttackRate()

      while(True):
        #challenger attack
        challengedHealth -= (challengerAttack - challengedBaseArmor) * challengerAttackRate
        if (challengedHealth <= 0):
          challenger.win()
          break


        #challenged attack
        challengerHealth -= (challengedAttack - challengerBaseArmor) * challengedAttackRate
        if(challengerHealth <= 0):
          challenged.win()
          break
        
        if(challengerHealthRegen != None):
          challengerHealth += challengerHealthRegen
        if(challengedHealthRegen != None):
          challengedHealth += challengedHealthRegen

      print("acabou uma batalha!")

vetWiner = []
for player in gg.getVertexList():
  vetWiner.append([player.getName(), player.getWin()])
  # print(player.getName(), end = " | ")
  # print(player.getWin())

vetWiner.sort(key = lambda x : x[1], reverse = True)

print(vetWiner)

