agenda = [
"ana",
"beto",
"carla",
"fernando",
"roberta",
"talys"
]
nome = "lucas"
i = 0

while agenda[i] != nome and i< len(agenda):
    i+=1

if agenda[i] == nome:
     print("existe")
else: print(" n existe")
