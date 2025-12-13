lista = [1,2,3,4,5,6,7,8,9,10]
valor = 8
soma = 0
i = 0
while i < len(lista) and i< valor:
    soma += lista[i]
    i+=1 

print(soma)
if soma >= valor:
    print("Sim")
else:
    print("Não")
