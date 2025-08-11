# Receba um número de quatro dígitos e forme um novo número com o último dígito colocado na frente (ex: 1234 → 4123).
num = int(input("Digite o número: "))

a = num//1000
num = num%1000

b = num//100
num = num%100

c= num//10
num= num%10

print(num,  a, b, c)