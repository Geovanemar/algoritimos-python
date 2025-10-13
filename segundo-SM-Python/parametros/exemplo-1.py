def concatena (**Kwargs):
    print(f"Valores recebidos: {Kwargs}")
    resultado = ""
    for valor in Kwargs.values():
        resultado += f"{valor}"
    return resultado

print(concatena(a = "Python", b = "Academy", c = "rules!!"))