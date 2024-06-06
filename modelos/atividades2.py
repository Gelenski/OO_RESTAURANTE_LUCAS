class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano


carro = Carro("Fusca", "Azul", 1974)
# print(vars(carro))


class Restaurante:
    def __init__(self, nome, categoria, preco):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        self.preco = preco
        self.qualidade = "Ótima"

    def __str__(self):
        return f"O restaurante {self.nome} serve {self.categoria}."


parada1 = Restaurante("Parada 1", "Prato Feito / Buffet", "Barato")
# print(vars(parada1))
# print(parada1)


class Cliente:
    def __init__(self, nome, sobrenome, possui_cartao, status):
        self.nome = nome
        self.sobrenome = sobrenome
        self.possui_cartao = possui_cartao
        self.status = status

    def __str__(self):
        return f"{self.nome} | {self.sobrenome} | {self.possui_cartao} | {self.status}"


paulo = Cliente("Paulo", "Gelenski", False, "Ativo")
joao = Cliente("João", "Batista", True, "Inativo")
cleverson = Cliente("Cleverson", "Silva", True, "Ativo")
# print(f"{paulo}\n{joao}\n{cleverson}")
