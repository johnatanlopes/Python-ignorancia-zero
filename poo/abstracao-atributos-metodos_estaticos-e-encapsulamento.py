'''
Métodos abstratos
'''
# Utilizando o pass para criar métodos abstratos
# A classe que herdar vai criar a regra do método da forma que desejar
class ObjetoGrafico(object):
    def __init__(self, cor):
        self.cor = cor

    def area(self):
        pass

    def perimetro(self):
        pass

    def info(self):
        print('%f metros serão preenchidos com a cor %s' % (self.area(), self.cor))

'''
Atributos e métodos estáticos
'''
# atributos estáticos do objeto cachorro
# O nome e a cor não são atributos da instância, mas sim da classe
class Cachorro(object):
    nome = 'Rex'
    cor = 'Marron'

dog = Cachorro()
print(dog.nome)
print(dog.cor)
print(Cachorro.nome)
print(Cachorro.cor)

# Criamos dois objetos e alteramos o atributo estatico em dois objetos
# O método estático não possui o self
class Conta(object):
    total = 10000
    reserva = 0.1
    def __init__(self, ID, saldo):
        self.ID = ID
        self.saldo = saldo

    def deposita(self, valor):
        self.saldo += valor
        Conta.total += self.saldo

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            Conta.total -= valor 

    def imprimeReserva():
        print(Conta.total * Conta.reserva)

conta1 = Conta(123, 5000)
conta1.deposita(1000)
conta1.saque(5000)
print(conta1.saldo)
print(conta1.total)

conta2 = Conta(123, 5000)
conta2.deposita(1000)
conta2.saque(5000)
print(conta2.saldo)
print(conta2.total)

Conta.deposita(conta2, 1000)
print(conta2.saldo)
print(conta2.total)


# conta2.imprimeReserva() # Retorna erro, pode ser chamado somentr atravez da classe
Conta.imprimeReserva()

'''
Encapsulamento

Utilizado para esconder os atributos e métodos
No python somente existe as permissões publico e privado, não existe protected

 - Ao colocar dois underscore na frente do atributo ele se torna privado
 - É possível acessar atributos privados de dentro de métodos publicos
'''

class Sistema(object):
    __permissao = 'total'
    def __init__(self, id):
        self.__id = id

    def exibePermissoes(self):
        print(Sistema.__permissao)
    
    def __getId(self):
        return self.__id

    def imprimeIdOutroMetodoPrivado(self):
        print(self.__getId())

sistema = Sistema(22)
sistema.exibePermissoes()

class LoginSistema(Sistema):
    def __init__(self, id):
        super().__init__(id)

loginSistema = LoginSistema(25)
loginSistema.imprimeIdOutroMetodoPrivado()



 