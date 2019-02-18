class Mamifero(object):
    def __init__(self, corDePelo, genero, numeroDePatas):
        self.corDePelo = corDePelo
        self.genero = genero
        self.numeroDePatas = numeroDePatas

    def falar(self):
        print('Ola sou um mamifera e eu sei falar')

    def andar(self):
        print('Estou andando sobre %i patas' % self.numeroDePatas)

    def amamentar(self):
        if self.genero.lower()[0] == 'm':
            print('Macho não amamentam')
        else:
            print('Amamentando meu filhote')

# Nosso cachorro
rex = Mamifero('marrom', 'masculino', 4)
rex.falar()
rex.andar()
rex.amamentar()

# Pessoa Julia
julia = Mamifero('preta', 'feminino', 2)
julia.falar()
julia.andar()
julia.amamentar()

# A classe que estamos criando abaixo herda de Mamifero
# Herdando todas as classes e atributos
class Pessoa1(Mamifero):
    pass


# Redefinindo a pessoa Julia
# Continuamos podendo acessar metodos da classe pai
julia = Pessoa1('preta', 'feminino', 2)
julia.falar()
julia.andar()
julia.amamentar()

# Rescrevendo o construtor, dessa forma ele não vai chamar o construtor do pai
class Pessoa2(Mamifero):
    def __init__(self):
        self.cabelo = 'Loiro'

julia = Pessoa2()

# Se tentar acessar o amamentar vai retornar erro pois não acessamos o construtor to Mamifero para
# passar os valores, isso se chama polimorfismo
# julia.amamentar()

# Rescrevendo um método
class Pessoa3(Mamifero):
    def __init__(self):
        self.cabelo = 'Loiro'
    
    def falar(self):
        print('Ola sou uma pessoa e eu sei falar')

julia = Pessoa3()
julia.falar()

 
# Utilizando o super no construtor e em um método
# o super pode ser chamado de duas formas:
#   super() vazio ou super(Pessoa, self)
class Pessoa4(Mamifero):
    def __init__(self, corDePelo, genero, numeroDePatas, cabelo):
        self.cabelo = cabelo
        super(Pessoa4, self).__init__(corDePelo, genero, numeroDePatas)
    
    def falar(self):
        super().falar()
        print('Ola sou uma pessoa e eu sei falar')

julia = Pessoa4('preta', 'feminino', '2', 'loiro')
print(julia.corDePelo)
julia.falar()