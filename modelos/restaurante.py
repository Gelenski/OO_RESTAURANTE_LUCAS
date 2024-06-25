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

# ! -------- Exercício 1 --------------

restaurante_praca.categoria = "Italiana"
# print(restaurante_praca.categoria)

# ! -------- Exercício 2 --------------

valo_nome = restaurante_praca.nome

# ! -------- Exercício 3 --------------

if restaurante_praca.ativo:
    print("Está ativo.")
else:
    print("Está inativo.")

# ! -------- Exercício 4 --------------

categoria = Restaurante.categoria

# ! -------- Exercício 5 --------------

restaurante_praca.nome = "Bistrô"
# print(restaurante_praca.nome)

# ! -------- Exercício 6 --------------

restaurante_pizza = Restaurante()
restaurante_pizza.nome = "Pizza Place"
restaurante_pizza.categoria = "Fast Food"

# ! -------- Exercício 7 --------------

if restaurante_pizza.categoria == "Fast Food":
    print("Está correto")
else:
    print("Não está correto")

# ! -------- Exercício 8 --------------

restaurante_pizza.ativo = True

# ! -------- Exercício 9 --------------

print(restaurante_praca.nome)
print(restaurante_praca.categoria)
