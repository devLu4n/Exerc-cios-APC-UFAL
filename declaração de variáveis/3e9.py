# Verificar se um número é múltiplo de 3, mas não de 9:
num = int(input("Digite o número: "))
verify = (num%3==0 and num&9!=0)
print(verify)