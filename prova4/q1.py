def letra_mais_frequente(arquivo):

    contagem = {}
    letra = 'a'
    while letra <= 'z':
        contagem[letra] = 0
        letra = chr(ord(letra) + 1)

    with open("texto.txt", "r", encoding="utf-8") as f:
        texto = f.read()

    for c in texto:
        c = c.lower()
        if 'a' <= c <= 'z':
            contagem[c] = contagem[c] + 1

    total = 0
    for l in contagem:
        total = total + contagem[l]

    if total == 0:
        return "nenhuma letra encontrada."

    mais_letra = None
    maior_qtd = -1
    for l in contagem:
        if contagem[l] > maior_qtd:
            maior_qtd = contagem[l]
            mais_letra = l

    porcentagem = (maior_qtd * 100.0) / total

    return f"{mais_letra} {porcentagem:.2f}%"

print(letra_mais_frequente("texto.txt"))