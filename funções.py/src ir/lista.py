from IR import ir
renda = [2000, 3000, 4000, 5000, 2455]

for i in renda:
    salario = i
    print(f"Seu IR de {salario} é: ", ir(salario))