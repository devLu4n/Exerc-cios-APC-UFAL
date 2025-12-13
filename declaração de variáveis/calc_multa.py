valor = float(input("Digite o valor do boleto: "))
multa = 2
dias = int(input("Digite o núemro de dias"))
juros = 0.05

total = valor + multa + (valor*juros*dias)
print("O valor total é: ", total)