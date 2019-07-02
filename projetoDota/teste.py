# importing the requests library 
import requests 
  
# api-endpoint 
URL = "https://api.opendota.com/api/heroStats"
  
# # location given here 
# location = "delhi technological university"
  
# # defining a params dict for the parameters to be sent to the API 
# PARAMS = {'address':location} 
  
# sending get request and saving the response as response object 
r = requests.get(url = URL) 
  
# extracting data in json format 
data = r.json()
for pers in data:
  print(pers["base_attack_min"])
