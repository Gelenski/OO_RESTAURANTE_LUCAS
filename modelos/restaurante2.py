class Restaurante:
    nome = ""
    categoria = ""
    ativo = False


restaurante_praca = Restaurante()
restaurante_praca.nome = "Praça"
restaurante_praca.categoria = "Gourmet"

restaurante_pizza = Restaurante()

restaurantes = [restaurante_praca, restaurante_pizza]
# print(restaurantes)
# print(restaurante_praca.ativo)
print(dir(restaurante_praca))
print()
print(vars(restaurante_praca))
