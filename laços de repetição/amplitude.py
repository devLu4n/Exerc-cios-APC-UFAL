lista = [7, 2, 9, 4, 5, 1, 3, 6, 8]
        
maior = lista[0]
menor = lista[0]    

for i in lista:
    if i > maior:
        maior = i
    if i < menor:
        menor = i

amplitude = maior - menor
print("A amplitude é:", amplitude)