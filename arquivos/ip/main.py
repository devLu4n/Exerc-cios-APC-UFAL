def validar_ip(ip: str) -> bool:
    ip = ip.strip()
    porcoes = ip.split('.')  # dividir por ponto

    if len(porcoes) != 4:
        return False

    for parte in porcoes:
        p = parte.strip()
        if not p.isdigit():           # cada parte deve conter apenas dígitos
            return False
        n = int(p)
        if not (0 <= n <= 255):       # verificar intervalo válido
            return False

    return True

if __name__ == "__main__":
    caminho = r"APC\arquivos\ip\ips.txt"
    with open(caminho, "r", encoding="utf-8") as file:
        for linha in file:
            ip = linha.strip()
            if not ip:
                continue
            print(f"{ip}: {validar_ip(ip)}")