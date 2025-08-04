# Sistema "Construção Fácil" - Código Completo em Python

# Estruturas de dados principais
produtos = []
clientes = []
vendedores = []
vendas = []

def cadastrar_produto():
    print("\n--- Cadastro de Produto ---")
    codigo = input("Código do produto: ")
    descricao = input("Descrição: ")
    categoria = input("Categoria (elétrica, hidráulica, etc): ")
    unidade = input("Unidade de medida (kg, m², saco...): ")
    preco_custo = float(input("Preço de custo: R$ "))
    preco_venda = float(input("Preço de venda: R$ "))
    estoque = int(input("Quantidade em estoque: "))
    estoque_min = int(input("Estoque mínimo: "))
    estoque_max = int(input("Estoque máximo: "))
    produtos.append({
        "codigo": codigo,
        "descricao": descricao,
        "categoria": categoria,
        "unidade": unidade,
        "preco_custo": preco_custo,
        "preco_venda": preco_venda,
        "estoque": estoque,
        "estoque_min": estoque_min,
        "estoque_max": estoque_max
    })
    print("Produto cadastrado com sucesso!\n")

def cadastrar_cliente():
    print("\n--- Cadastro de Cliente ---")
    nome = input("Nome do cliente: ")
    telefone = input("Telefone: ")
    cpf = input("CPF: ")
    clientes.append({
        "nome": nome,
        "telefone": telefone,
        "cpf": cpf
    })
    print("Cliente cadastrado com sucesso!\n")

def cadastrar_vendedor():
    print("\n--- Cadastro de Vendedor ---")
    nome = input("Nome do vendedor: ")
    matricula = input("Matrícula: ")
    vendedores.append({
        "nome": nome,
        "matricula": matricula
    })
    print("Vendedor cadastrado com sucesso!\n")

def registrar_venda():
    print("\n--- Registrar Venda ---")
    cliente_nome = input("Nome do cliente (ou deixe em branco se não cadastrado): ")
    vendedor_nome = input("Nome do vendedor: ")
    data = input("Data da venda (dd/mm/aaaa): ")
    itens = []
    total_venda = 0.0
    while True:
        cod_produto = input("Código do produto (ou 'fim' para encerrar): ")
        if cod_produto.lower() == "fim":
            break
        produto = next((p for p in produtos if p["codigo"] == cod_produto), None)
        if not produto:
            print("Produto não encontrado.")
            continue
        quantidade = int(input("Quantidade: "))
        if quantidade > produto["estoque"]:
            print("Estoque insuficiente.")
            continue
        desconto = float(input("Desconto em R$ (se houver): "))
        valor_unit = produto["preco_venda"]
        subtotal = (valor_unit * quantidade) - desconto
        produto["estoque"] -= quantidade
        itens.append({
            "produto": produto["descricao"],
            "quantidade": quantidade,
            "valor_unitario": valor_unit,
            "desconto": desconto,
            "subtotal": subtotal
        })
        total_venda += subtotal
    pagamento = input("Forma de pagamento (dinheiro, cartão, pix): ").lower()
    if pagamento in ["dinheiro", "pix"]:
        comissao = total_venda * 0.05
    else:
        comissao = total_venda * 0.03
    vendas.append({
        "cliente": cliente_nome or "Não cadastrado",
        "vendedor": vendedor_nome,
        "data": data,
        "itens": itens,
        "total": total_venda,
        "comissao": comissao,
        "pagamento": pagamento
    })
    print(f"\nVenda registrada! Total: R$ {total_venda:.2f} | Comissão: R$ {comissao:.2f}\n")

def relatorios():
    print("\n=== RELATÓRIOS ===")
    if not vendas:
        print("Nenhuma venda registrada.\n")
        return
    total_geral = sum(v["total"] for v in vendas)
    print(f"Total de vendas: R$ {total_geral:.2f}")
    
    print("\nComissões por vendedor:")
    comissoes = {}
    for v in vendas:
        comissoes[v["vendedor"]] = comissoes.get(v["vendedor"], 0) + v["comissao"]
    for vendedor, valor in comissoes.items():
        print(f" - {vendedor}: R$ {valor:.2f}")
   
    print("\nProdutos mais vendidos:")
    vendas_prod = {}
    for v in vendas:
        for item in v["itens"]:
            nome = item["produto"]
            vendas_prod[nome] = vendas_prod.get(nome, 0) + item["quantidade"]
    for nome, qtde in sorted(vendas_prod.items(), key=lambda x: x[1], reverse=True):
        print(f" - {nome}: {qtde} unidades")
    print()

def alertas_estoque():
    print("\n=== ALERTAS DE ESTOQUE ===")
    for p in produtos:
        if p["estoque"] < p["estoque_min"]:
            print(f"[BAIXO] {p['descricao']}: {p['estoque']} (< mínimo {p['estoque_min']})")
        elif p["estoque"] > p["estoque_max"]:
            print(f"[EXCEDENTE] {p['descricao']}: {p['estoque']} (> máximo {p['estoque_max']})")
    print()

def listar_estoque():
    print("\n=== ESTOQUE ATUAL ===")
    if not produtos:
        print("Nenhum produto cadastrado.\n")
        return
    for p in produtos:
        print(f"{p['codigo']} - {p['descricao']}: {p['estoque']} {p['unidade']}")
    print()

def menu():
    while True:
        print("=== CONSTRUÇÃO FÁCIL ===")
        print("1. Cadastrar Produto")
        print("2. Cadastrar Cliente")
        print("3. Cadastrar Vendedor")
        print("4. Registrar Venda")
        print("5. Relatórios")
        print("6. Alertas de Estoque")
        print("7. Listar Produtos")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            cadastrar_cliente()
        elif opcao == "3":
            cadastrar_vendedor()
        elif opcao == "4":
            registrar_venda()
        elif opcao == "5":
            relatorios()
        elif opcao == "6":
            alertas_estoque()
        elif opcao == "7":
            listar_estoque()
        elif opcao == "0":
            print("Encerrando sistema.")
            break
        else:
            print("Opção inválida!\n")

if __name__ == "__main__":
    menu()
