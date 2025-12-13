palavra = "algoritmo"
reverso = ""

for i in range(len(palavra)-1, 0-1, -1):
    reverso += palavra[i]
    print(i, palavra[i])
    
print(reverso)