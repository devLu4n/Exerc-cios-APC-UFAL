# Área do triângulo retângulo
'''
base = float(input("Digite o valor da base: "))
altura = float(input("Digite o valor da altura: "))
area = ((base * altura)/2)

print("A área do triângulo é: ", area)'''

# Média do aluno
'''
ab1 = float(input("Digite a nota 1: "))
ab2 = float(input("Digite a nota 2: "))
ab3 = float(input("Digite a nota 3: "))
ab4 = float(input("Digite a nota 4: "))
media = ((ab1 + ab2 + ab3 + ab4)/4)
print("A média do aluno é: ", media)'''

# Impar ou par
'''
num = int(input("Digite o número: "))
print(num % 2 == 0)'''

# Conversor de temperatura
'''
f = float(input("Digite sua temperatura em F°: "))
celsius = (f-32)/1.8
print("Sua temperatura em Celsius é:", round(celsius,2),'°C')
'''

# Conversor de moeda
'''
dol = float(input("Digite seu valor em dólar: "))
cambio = float(input("Digite a taxa de cambio do dia vigente: "))

print("convertendo, seu valor em real é: R$", (dol*cambio))
'''

# Área da circunferência
'''
raio = float(input("Digite o valor do raio: "))
C = (2*3.14*raio)
print("O valor da circunferência é: ", C)
'''

# Multa
'''
valor = float(input("Digite o valor do boleto: "))
multa = 2
dias = int(input("Digite o núemro de dias"))
juros = 0.05

total = valor + multa + (valor*juros*dias)
print("O valor total é: ", total)
'''

# Conversor de horas
''''
tempo = int(input("Digite seu valor : "))
horas = tempo//60
min = tempo%60

print('São', horas, ":", min, "h")
'''

# Verificador ano bissexto
'''
ano = int(input("Declare o valor do ano: "))
divisao =  (ano%4==0 and ano%100!=0) or (ano%400==0)
print(divisao)
'''

# Numeros invertidos
'''
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
'''

# Trocar valores
'''
a = int(input("Digite o valor a: "))
b = int(input("Digite o valor b: "))

a = a+b
b = a-b
a = a-b

print(a, b)
'''


