#Exemplo 1
class MinhaClasse:
    x = 5
    print(MinhaClasse)


p1 = MinhaClasse()
print(p1.x)


#Exemplo 2
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa("Maria", 25)

print('nome: ', p1.nome)
print('Idade: ', p1.idade)


#Exemplo 3
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def imprimir(self):
        print("Nome: ", self.nome)
        print("Idade: ", self.idade)

p1 = Pessoa("Maria", 25)
p1.imprimir()