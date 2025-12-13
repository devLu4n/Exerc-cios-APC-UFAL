def vogais(palavra):

    vogais = {"a":0,"e":0, "i":0,"o":0,"u":0}

    for i in palavra.lower():
        if i in vogais: 
            vogais[i] = vogais[i]+1
    return vogais
    

palavra = "paralelepipedo"
print(vogais(palavra))