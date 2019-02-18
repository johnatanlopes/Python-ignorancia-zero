'''
Podemos iniciar uma classe de três formas:

    class MeuObjeto:
    class MeuObjeto():
    class MeuObjeto(object):
    O mais correto é utilizar a última opção

Quando criamos a classe devemos criar o construtor
    
    def __init__(self)

O self quer dizer que estamos nos referenciando ao proprio objeto que no nosso caso se chama MeuObjeto
O construtor e os métodos não se limitam somente a self, pode ser adicionado outras informações

Se no parametro adicionarmos um valor recebendo 0 ele é opcional

Também no parametro podemos utilizar *args para receber várias valores pelo método
'''

class MeuObjeto(object):
    # Criando nosso construtor
    def __init__(self, profissao, salario = 0):
        self.nome = 'Johnatan'
        self.idade = 29
        self.profissao = profissao
        self.salario = salario
        print('Construtor chamado com sucesso')

    # Criando o método
    def imprime(self, x, *args):
        print('Ola meu nome é %s e eu tenho %d anos' % (self.nome, self.idade))
        print(x)
        print(args)

    def getProfissao(self):
        print(self.profissao)

    def setSalario(self, salario):
        print("Eu ganho " + str(salario))

# Executando
obj = MeuObjeto('desenvolvedor')
obj.imprime(1, 2, 3, 4, 5)
obj.getProfissao()
obj.setSalario(12000)