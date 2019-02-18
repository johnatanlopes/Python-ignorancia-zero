class Minha(object):
    def __init__(self):
        self.x = 0
        self.y = 0

# Sem encapsular os atributos podemos passar valores diretamente para eles
meu = Minha()
print(meu.x)

meu.x = 5
print(meu.x)

# Exemplo de associação
class PessoaAmaAnimais(object):
    def __init__(self, nome, peso, cao):
        self.nome = nome
        self.peso = peso
        self.cao = cao

    def treinar(self):
        self.cao.daApatinha()
        self.cao.latir()

class Cachorro(object):
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def daApatinha(self):
        print('%s extendeu a patinha' % self.nome)

    def latir(self):
        print('AUAUAUAUAUAUAUAU!')

rex = Cachorro('Rex', 'Marrom')
pessoa = PessoaAmaAnimais('Johnatan', 100, rex)
print(pessoa.cao.cor)
pessoa.treinar()

# Se alterarmos o valor de uma tributo dentro de uma def forá da função o valor continuará existindo
def mudaNome(nome):
    pessoa.nome = nome

mudaNome('José')
print(pessoa.nome)