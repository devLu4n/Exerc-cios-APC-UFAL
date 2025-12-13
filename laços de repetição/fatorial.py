'''num =  int(input("Digite um número para calcular o fatorial: "))
fatorial = 1            
i = 0
while i < num:
    i += 1
    fatorial *= i '''

num =  int(input("Digite um número para calcular o fatorial: "))
mult = 1

while num >= 1:
    mult *= num
    num -= 1

print("O fatorial é: ", mult)