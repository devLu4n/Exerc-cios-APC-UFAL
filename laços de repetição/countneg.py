lista = [-1, 2, 5, -12, 24, 32, -22, 73, -2]
count = 0

for i in lista:
    if i < 0:
        count+=1

print("a quantidade de números negativos na lista é: ", count)