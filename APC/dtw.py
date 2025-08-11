# Conversor de dia para semana
dias = int(input("Digite a quantidade de dias: "))
semana = dias//7 
result = dias%7

print("No total são:", semana, "semana(s) e ", result, "dias")