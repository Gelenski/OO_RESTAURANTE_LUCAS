class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f"{self.nome} | {self.categoria} | {self.ativo}"

    @classmethod
    def listar_restaurantes(cls):
        print(f"Nome do restaurante | Categoria | Ativo")
        for restaurante in cls.restaurantes:
            print(f"{restaurante.nome} | {restaurante.categoria} | {restaurante._ativo}")

    @property
    def ativo(self):
        return "☒" if self._ativo else "☐"


restaurante_praca = Restaurante("Praça", "Gourmet")
restaurante_pizza = Restaurante("pizza express", "Italiana")

Restaurante.listar_restaurantes()
