def search(texto):
    dicionario = {}
    palavras = texto.lower().split()
    for i in palavras:
        if i in dicionario:
            dicionario[i] +=1
        else: dicionario[i] = 1
    return dicionario
        
texto = input("Digite seu texto: ")

resultado = search(texto)
print(resultado)
