# Cálculo do salário de funcionários

def calcular_salario(horas_trabalhadas: float, valor_hora: float) -> float:
    if horas_trabalhadas <= 40:
        salario = horas_trabalhadas * valor_hora
    else:
        horas_extras = horas_trabalhadas - 40
        salario = (40 * valor_hora) + (horas_extras * valor_hora * 1.5)
    return salario

# Exemplo de uso:
funcionarios = [
    {"nome": "Ana", "horas": 38, "valor_hora": 20},
    {"nome": "Bruno", "horas": 45, "valor_hora": 18},
    {"nome": "Carlos", "horas": 40, "valor_hora": 22},
    {"nome": "Diana", "horas": 50, "valor_hora": 25}
]

for f in funcionarios:
    salario = calcular_salario(f["horas"], f["valor_hora"])
    print(f'{f["nome"]}: R$ {salario:.2f}')