def filtrar_n(nomes):
    return [nome for nome in nomes if len(nome) > 5]

nomes = ["gabriel", "geovane", "sofia", "yudi", "camilla", "arthur"]
print(filtrar_n(nomes))