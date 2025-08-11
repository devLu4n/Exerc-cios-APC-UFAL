# Receba um número de quatro dígitos e calcule o produto entre o primeiro e o último dígito.

num = int(input("Digite o número: "))

a = num//1000
num = num%1000

b = num//100
num = num%100

c = num//10
num = num % 10

print(a*num)
