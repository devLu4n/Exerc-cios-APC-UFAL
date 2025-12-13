# Receba um número de quatro dígitos (ex: 1234) e inverta apenas os dois últimos dígitos, resultando em 1243.
num = int(input("Digite o número: "))

a = num//1000
num = num%1000

b = num//100
num = num%100

c = num//10
num= num%10

print(a, b, num, c)