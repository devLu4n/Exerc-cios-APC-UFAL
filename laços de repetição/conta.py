conta = 0

while True:
    saldo = input("Digite o valor do saldo: ")

    if saldo == "":
        break

    conta += int(saldo)

print("O valor total da conta é: ", conta)  
    