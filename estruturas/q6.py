def verificar_cartela(cartela, sorteados):
    for letra, numeros in cartela.items():
        coluna_completa = True

        for numero in numeros:
            if numero not in sorteados:
                coluna_completa = False 
                break  

        if coluna_completa:
            return True  # Alguma coluna está completa

    return False  # Nenhuma coluna está completa

cartela = {
    'B': [5, 10, 2, 7, 1],
    'I': [16, 22, 18, 20, 17],
    'N': [31, 33, 34, 36, 35],
    'G': [46, 50, 48, 47, 49],
    'O': [61, 65, 63, 62, 64]
}


sorteados = [5, 10, 2, 7, 1, 16, 18, 20, 17]

resultado = verificar_cartela(cartela, sorteados)
print(resultado)