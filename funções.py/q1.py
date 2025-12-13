def encontrar_maior(lista):
    maior = lista[0]
    for i in lista[1:]:
        if i > maior:
            maior = i

lista = [1,2,3,4,5,6,7,8,9,10]
encontrar_maior(lista)