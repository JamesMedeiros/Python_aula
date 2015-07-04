#criaçao da classe
class Pessoa (object):
    #declaraçao de atributo da classe
    nome = ""
    idade = 0

    def __init__(self, nome):
        self.nome = nome

        
    #criaçao do metodo
    def andar(self):
        print ("A pessoa esta andando...")
        
#instanciamos o objeto
p = Pessoa("James Medeiros")
#definimos o valor do atributo nome
p.nome = "James Medeiros"
#definimos o valor da idade
p.idade = 36
#faz a impressao dos valores do atributo
print("Nome: ", p.nome, "Idade: ", p.idade)
p.andar()
