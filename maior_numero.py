num = float(input("Digite seu 1° número:  "))
num2 = float(input("Digite seu 2° número: "))

if (num and num2)==0:
    print("O número é invalido")

'''if num>num2:
    print(num)
else: 
    print(num2)'''

print(num) if num>num2 else print(num2)