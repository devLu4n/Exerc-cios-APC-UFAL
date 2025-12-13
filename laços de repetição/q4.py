lista = [2,4,7,1,10]

maior = lista[0]
menor = lista[0]

for i in lista:
    if i > maior:
        maior = i
    elif i < menor:
        menor = i
amplitude = maior - menor
print("A amplitude da lista é:", amplitude,", sendo o maior e menor, respectivamente:", maior, "e", menor )