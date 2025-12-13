lista = [1, 3, 5, 8, 6, 7, 4]
n1 = 5
n2 = 8

for i in range(len(lista)):

    if lista[i] == n1  and lista[i+1] == n2:
        print("estão em sequência")
    else: print('Não estão em sequência')