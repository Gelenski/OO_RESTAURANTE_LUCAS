class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

    def __str__(self):
        return f"{self.nome} | {self.categoria} | {self.ativo}"


restaurante_praca = Restaurante("Praça", "Gourmet")

# restaurante_praca = Restaurante()
# restaurante_praca.nome = "Praça"
# restaurante_praca.categoria = "Gourmet"

# print(restaurantes)
# print(restaurante_praca.ativo)
# print(dir(restaurante_praca))
# print()
print(vars(restaurante_praca))
