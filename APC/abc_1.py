'''Receba três números inteiros nas variáveis a, b e c. Troque os valores de forma que:

a receba o valor de b,

b receba o valor de c,

c receba o valor original de a.'''
n1 = int(input("Digite o 1° número: "))
n2 = int(input("Digite o 2° número: "))
n3 = int(input("Digite o 3° número: "))

n1 = n1+n2
n2 = n1 - n2
n1 = n1 - n2
n3 = n2 + n3
n3 = n3 - n1
print (n1, n2, n3)