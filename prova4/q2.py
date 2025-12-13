import os

def cartela_vencedora(sequencia, arquivo):
  
    cartela = []
    base = os.path.abspath(os.path.dirname(__file__))
    caminho = os.path.join(base, arquivo)

    with open(caminho, "r", encoding="utf-8") as f:
        for linha in f:
            valores = linha.strip().split()
            if not valores:
                continue
            linha_numeros = [int(v) for v in valores]
            cartela.append(linha_numeros)

    if not cartela:
        return False

    rows = len(cartela)
    cols = len(cartela[0])
    for r in cartela:
        if len(r) != cols:
            raise ValueError("cartela com linhas de tamanhos diferentes")

    for coluna in range(cols):
        if all(cartela[linha][coluna] in sequencia for linha in range(rows)):
            return True  # Achou uma coluna completa -> cartela vencedora

    return False 

seq1 = {10,7,17,42,24,90,53,51,44,67,74,86}
seq2 = {10,6,12,42,24,90,53,44,67,74,86,88}

print("sequencia1:", "cartela vencedora" if cartela_vencedora(seq1, "bingo.txt") else "cartela não vencedora")
print("sequencia2:", "cartela vencedora" if cartela_vencedora(seq2, "bingo.txt") else "cartela não vencedora")
