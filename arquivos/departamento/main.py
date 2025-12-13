import csv
from pathlib import Path

def media_salarial_por_departamento(caminho_csv: str) -> None:
    totais = {}
    contagens = {}

    with open(caminho_csv, 'r', encoding='utf-8') as f:
        linhas = f.read().splitlines()

    if not linhas:
        print("Arquivo vazio ou não encontrado.")
        return

    # pula cabeçalho
    for linha in linhas[1:]:
        if not linha.strip():
            continue

        partes = linha.split(',')
        if len(partes) < 6:
            continue

        departamento = partes[4].strip()
        salario = partes[5].strip()
        if not departamento or not salario:
            continue

        salario = salario.replace('$', '').replace(',', '')
        try:
            valor = float(salario)
        except ValueError:
            continue

        if departamento in totais:
            totais[departamento] += valor
            contagens[departamento] += 1
        else:
            totais[departamento] = valor
            contagens[departamento] = 1

    for departamento in sorted(totais):
        media = totais[departamento] / contagens[departamento]
        print(f"{departamento}: ${media:,.2f}")

if __name__ == "__main__":
    csv_path = "dados/MOCK_DATA (1).csv"
    media_salarial_por_departamento(csv_path)