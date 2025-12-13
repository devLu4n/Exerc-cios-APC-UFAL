valor = int(input("Digite o valor a ser sacado: "))

n100 = valor // 100
valor %= 100

n50 = valor // 50
valor %= 50

n10 = valor // 10
valor %= 10

n5 = valor // 5
valor %= 5

n1 = valor // 1
valor %= 1

# Exibe o resultado
print("Notas fornecidas:")
if n100 > 0:
    print(f"{n100} nota(s) de R$ 100")
if n50 > 0:
    print(f"{n50} nota(s) de R$ 50")
if n10 > 0:
    print(f"{n10} nota(s) de R$ 10")
if n5 > 0:
    print(f"{n5} nota(s) de R$ 5")
if n1 > 0:
    print(f"{n1} nota(s) de R$ 1")