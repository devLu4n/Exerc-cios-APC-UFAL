def organizar(dados):
    dicionario = {}
    for funcionario, setor in dados:
        if setor in dicionario:
            dicionario[setor].append(funcionario)
        else: dicionario[setor]= [funcionario]
    return dicionario

dados = [
    ("João", "TI"),
    ("Maria", "RH"),
    ("Pedro", "TI"),
    ("Ana", "Financeiro"),
    ("Clara", "RH")]

resultado = organizar(dados)
print(resultado)