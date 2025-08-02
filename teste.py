lista_precos = ["10", "200", "50", "300", "218"]

for preco in lista_precos:
    preco_num = float(preco)
    imposto = preco_num * 0.2
    print(imposto)