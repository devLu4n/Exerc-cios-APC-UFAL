'''
Validar CPF
9 primeiros digitos, multiplica decrescente de 10 a 2
some o resultado
calcule o resto da divisão por 11
se o resto for menor que 2, o primeiro digito é 0
se for maior ou igual a 2, o digito é 11 - resto

etapa 2
pegue os 9 primeiros digitos e o 1 verificador
multiplica os 10, descrescente do 11 a 2
some o resultado
calcule o resto da divisão por 11

'''
cpf = [1,2,3,4,5,6,7,8,9,1,0] 
p = 10
soma = 0
for i in cpf[:9]:
   print(i*p)
   soma += i * p
   p = p-1
   
print(soma)
resto = soma%11
if resto < 2:
   print("Primeiro digito: 0")
   digito1= 0
else: digito1 = 11 - resto