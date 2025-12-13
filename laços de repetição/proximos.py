lista = [1, 3, 5, 8, 6, 7, 4]
n1= 5
n2 = 9

for i in range(len(lista)-1):
    if n1 == lista[i] and n2 == lista[i+1]:
        print("Estão em sequência")
    else: print("Não estão em sequencia")