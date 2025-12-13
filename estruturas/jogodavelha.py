def verificar_vencedor(tabuleiro):
    for linha in tabuleiro:
        if linha[0] == linha[1] == linha[2] and linha[0] != ' ':
            return f"{linha[0]} vencedor"

    for c in range(3):
        if tabuleiro[0][c] == tabuleiro[1][c] == tabuleiro[2][c] and tabuleiro[0][c] != ' ':
            return f"{tabuleiro[0][c]} vencedor"

    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro[0][0] != ' ':
        return f"{tabuleiro[0][0]} vencedor"

    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] and tabuleiro[0][2] != ' ':
        return f"{tabuleiro[0][2]} vencedor"

    return "empate"

exemplo1 = [
    ['O', 'X', 'O'],
    ['X', 'X', 'O'],
    ['O', 'X', 'X']
]

exemplo2 = [
    ['O', 'X', 'O'],
    ['X', 'X', 'O'],
    ['O', 'O', 'X']
]

print(verificar_vencedor(exemplo1)) 
print(verificar_vencedor(exemplo2)) 
