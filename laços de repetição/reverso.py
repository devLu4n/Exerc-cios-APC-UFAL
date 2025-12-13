nome = "Abracadabra"
reverso = ''

for i in nome:
    reverso = i + reverso

print(reverso)

'''
nome = "Abracadabra"

for i in range(len(nome)-1, -1, -1):
    print(nome[i], end='') 
    '''