# 1
# class Pessoa:
#     def __init__(self, nome, idade, profissao):
#         self.nome = nome
#         self.idade = idade
#         self.profissao = profissao
    
#     def aniversario(self):
#         self.idade += 1
    
#     def __str__(self):
#         return f"Nome: {self.nome}, Idade: {self.idade}, Profissão: {self.profissao}"       
    
#     @property
#     def saudacao(self):
#          print(f"**{self.profissao}**")

    
# lucas = Pessoa("Lucas", 16, "Estudante")
# lucas.aniversario()
# print(lucas)
# lucas.saudacao


# # 2
# class ContaBancaria:
#     def __init__(self, titular, saldo):
#         self.titular = titular 
#         self.saldo = saldo
#         self.ativo = False
# # 3
#     def __str__(self):
#         return f"Titular:{self.titular}, Saldo: R${self.saldo}, Status: {self.ativo}"
# #4
#     def ativar_conta(self):   
#         self.ativo = not self.ativo 
        

# lucas = ContaBancaria("Lucas", 10000)
# fernanda = ContaBancaria("Fernanda", 20000) 
# fernanda.ativar_conta()
# print(lucas)
# print(fernanda) 

# 6
# class ClienteBanco:
#     clientes_banco = []

#     def __init__(self, nome, idade, saldo, ativo, cerasa):
#         self.nome = nome
#         self.idade = idade
#         self.saldo = saldo
#         self.ativo = ativo
#         self.cerasa = cerasa
#         ClienteBanco.clientes_banco.append(self)
    
#     @classmethod
#     def lista_devedores(cls):
#         print("Esses devem:")
#         for clientes in cls.clientes_banco:
#             print(clientes.nome, "|" ,"Deve" if clientes.cerasa else "Não deve")

    

# teresa = ClienteBanco("Teresa", 80, 80000, True, False)
# patrick = ClienteBanco("Patrick", 30, 2000, False, False)
# desiderio = ClienteBanco("Desiderio", 92, 0, True, True)

# ClienteBanco.lista_devedores()