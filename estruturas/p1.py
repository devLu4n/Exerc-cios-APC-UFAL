def vogais(palavra):
    vogais = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for vogal in palavra.lower():
        if vogal in vogais:
            vogais[vogal] += 1
    return vogais

if __name__ == "__main__":
    palavra = "Paralelepipedo"
    print(vogais(palavra))
