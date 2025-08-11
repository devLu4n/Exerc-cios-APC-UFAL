# Receba um número de três dígitos (ex: 123) e forme um número de seis dígitos espelhando os dígitos, resultando em 123321.

num = int(input("Digite o número: "))

a = num//100
num = num % 100

b = num//10
num = num%10

print(a, b, num, num, b, a)