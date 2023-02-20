import json
from tabulate import tabulate
with open('C:/Users/modik/Documents/pp2/4lab/json/data.json', 'r') as file:
    data = json.load(file)

print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU  ")
print("-------------------------------------------------- --------------------  ------  ------")
for j in range(18):
    for i in data["imdata"][j]["l1PhysIf"]["attributes"]:
        print(i[0])

