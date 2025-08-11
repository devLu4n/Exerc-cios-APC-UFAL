num = int(input("Digite o número: "))

n1 = num//100
num = num%100

n2= num//10
num = num %10

print(n1+n2+num)