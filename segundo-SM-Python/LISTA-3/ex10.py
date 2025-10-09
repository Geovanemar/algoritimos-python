class Nota_Fiscal:
    def __init__(self, numero, tipo, serie, cnpj, razao_social, data, valor_produto, icms, frete, ipi):
        self.numero = numero
        self.tipo = tipo
        self.serie = serie
        self.cnpj = cnpj
        self.razao_social = razao_social
        self.data = data
        self.valor_produto = valor_produto
        self.icms = icms
        self.frete = frete
        self.ipi = ipi
        self.valor_total = 0.0

    def obterNumero(self):
        print(f"Número da Nota Fiscal: {self.numero}")
        return self.numero

    def obterDataEmissao(self):
        print(f"Data de Emissão: {self.data}")
        return self.data

    def alterarRazaoSocial(self, nova_razao_social):
        self.razao_social = nova_razao_social
        print(f"Razão social alterada para: {self.razao_social}")

    def calcularValorTotal(self):
        self.valor_total = self.valor_produto + self.icms + self.frete + self.ipi
        print(f"Valor total da nota fiscal: R$ {self.valor_total:.2f}")
        return self.valor_total


nf1 = Nota_Fiscal(
    numero=1234,
    tipo="Saída",
    serie=1,
    cnpj="12.345.678/0001-99",
    razao_social="Construção Fácil Ltda.",
    data="08/10/2025",
    valor_produto=1500.00,
    icms=270.00,
    frete=80.00,
    ipi=60.00
)

print("\n--- Dados da Nota Fiscal ---")
nf1.obterNumero()
nf1.obterDataEmissao()
nf1.calcularValorTotal()
nf1.alterarRazaoSocial("Construção Fácil Materiais de Construção Ltda.")
