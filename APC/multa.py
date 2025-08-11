valor = int(input("Digite o valor: "))
multa = 2
dias = int(input("Digite a quantidade de dias em atraso: "))
juros = 0.05
total = valor + multa + (valor*juros*dias)
print(total)