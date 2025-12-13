alfabeto = ["a","b", 'c', 'd', 'e', 'f', 'g', 'h', 'i','j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's','t', 'u', 'v', 'w', 'x', 'y', 'z']
k = 3
letra_buscada = "c"

#encontrar posição
encontrou = False
p = 0
for letra in alfabeto:
    if not encontrou:
        p+=1
    if letra == letra_buscada:
        encontrou= True
        break
    novo_indice = (p+k) %26

        #O encontrou começa falso, ou seja, se nao encontrei, eu começo a incrementar a posição
        #Quando eu encontrar a letra buscada, eu mudo o encontrou para verdadeiro e saio do laço, imprimindo p
print(p)
p = p + k
print(alfabeto[p])



    