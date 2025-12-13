if __name__ == "__main__":
    contato = {
        'nome': 'João',
        'telefone': [12345678, 98765432, 11223344],
        'email': 'joao@gmail.com'
    }
    print(contato)
    print(contato['telefone'][0])

    for key in contato:
        print(key, contato[key])

    nomes = {}

    nomes["nome1"] = "Ana"
    nomes["nome2"] = "Bob"
    nomes["idade1"] = 19
    nomes["idade2"] = 18

    for key in sorted(nomes):
        print(key, nomes[key])