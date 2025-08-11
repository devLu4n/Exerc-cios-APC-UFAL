valor = int(input("Digite o número: "))
m = valor // 1000
valor = valor % 1000

c = valor//100
valor = valor % 100

d = valor//10
valor= valor%10

u = valor//1
valor%1

print(u, d, c, m)