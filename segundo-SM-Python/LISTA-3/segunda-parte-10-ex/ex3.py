class Pessoa:
    def __init__(self, nome, telefone, email, endereco):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def negociar(self):
        print(f"{self.nome} está realizando uma negociação.")


class PessoaFisica(Pessoa):
    def __init__(self, nome, telefone, email, endereco, cpf):
        super().__init__(nome, telefone, email, endereco)
        self.cpf = cpf

    def apresentar_documento(self):
        print(f"Pessoa Física: {self.nome} - CPF: {self.cpf}")

    def assinar_contrato(self):
        print(f"{self.nome} assinou o contrato como pessoa física.")


class PessoaJuridica(Pessoa):
    def __init__(self, nome, telefone, email, endereco, cnpj):
        super().__init__(nome, telefone, email, endereco)
        self.cnpj = cnpj

    def apresentar_documento(self):
        print(f"Pessoa Jurídica: {self.nome} - CNPJ: {self.cnpj}")

    def emitir_nota_fiscal(self):
        print(f"{self.nome} emitiu uma nota fiscal como pessoa jurídica.")



if __name__ == "__main__":
    pf = PessoaFisica("Maria Silva", "99999-8888", "maria@gmail.com", "Rua das Flores, 123", "123.456.789-00")
    pj = PessoaJuridica("Tech Solutions LTDA", "3333-4444", "contato@techsol.com", "Av. Central, 500", "12.345.678/0001-90")

    pf.negociar()
    pf.apresentar_documento()
    pf.assinar_contrato()
    print()

    pj.negociar()
    pj.apresentar_documento()
    pj.emitir_nota_fiscal()
