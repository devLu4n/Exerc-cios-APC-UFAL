age = int(input("Digite sua idade: "))

if (age<=0):
    print("Inválido")
elif(1<= age < 14):
    print("Criança")
elif (14 <= age <17):
    print("Adolescente")
elif (18 <= age <= 59):
    print("Adulto")
else: 
    print("Idoso")