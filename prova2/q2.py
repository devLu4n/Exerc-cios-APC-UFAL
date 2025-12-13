peso = [64, 55, 78, 90]
altura = [1.55, 1.67, 1.90, 1.85]

for i in range(len(peso)):
    imc = peso[i]/(altura[i]**2)
    print(imc)
    if imc < 18.49:
        print("abaixo do peso")
    elif imc >= 18.5 and imc <= 24.99:
        print("Peso normal")
    elif imc >= 25 and imc<= 29.99:
        print("Acima do peso")
    else:
        print("Obesidade")

