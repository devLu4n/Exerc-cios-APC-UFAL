#  Você está trabalhando em um programa de codificação de caracteres. Atualmente você está 
# trabalhando com o código UTF8, que relaciona letras e códigos como descrito na tabela abaixo. Implemente
#um programa que recebe uma lista de códigos UTF8 e decodifique para a linguagem natural.
utf8cod = {
    '61': 'a', '62': 'b', '63': 'c', 
    '64': 'd', '65': 'e', '66': 'f', 
    '67': 'g', '68': 'h', '69': 'i',
    '6a': 'j', '6b': 'k', '6c': 'l', 
    '6d': 'm', '6e': 'n', '6f': 'o', 
    '70': 'p', '71': 'q', '72': 'r',
    '73': 's', '74': 't', '75': 'u', 
    '76': 'v', '77': 'w', '78': 'x', 
    '79': 'y', '7a': 'z', '20': ' '
}

def decodificador(codigos):
    mensagem = ""
    for codigo in codigos:
        codigo = codigo.lower()
        if codigo in utf8cod:
            mensagem += utf8cod[codigo]
        else:
            mensagem += "" 
    return mensagem

entrada = ['65','75','20','61','6d','6f','20','70','72','6f','67','72','61','6d','61','72']
entrada2 = ['6c', '75','61', '6e']
print(decodificador(entrada))
print(decodificador(entrada2))
