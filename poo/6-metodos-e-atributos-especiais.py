
class Conta(object):
    """
    objeto do tipo Conta que representa uma conta
    """
    def __init__(self, id, saldo):
        """
        Construtor da classe conta
        """
        self.id = id
        self.saldo = saldo

    # o método especial __str__ retorna uma string ao imprimir o objeto sem chamad nenhum método
    def __str__(self):
        """
        Imprime o objeto Conta
        """
        return 'ID: %i\nSaldo: R$ %.2f' % (self.id, self.saldo)
    
    # O add espera receber um outro objeto, para fazer a soma é só chamar objeto + objeto
    # __add__ somando objetos, 
    # __sub__ subtraindo objetos
    # __div__ dividindo objetos
    # __mult__ multiplicando objetos
    def __add__(self, outraConta):
        self.saldo += outraConta.saldo

# Utilizando o __str__
bradesco = Conta(456, 5000)
print(bradesco)

# Somando objetos com __add__
itau = Conta(123, 8000)
itau + bradesco
print(itau)

# Podemos imprimir uma conta por meio de dicionario
print(itau.__dict__)

# O __doc__ contém a descrição de construtores, métodos, atributos
# Se não possuir o comentário o doc traz vazio
print(itau.__doc__)
print(itau.__init__.__doc__)
print(itau.__str__.__doc__)

# Exibindo a documentação da sua classe
#help(itau)


# Verificando se uma classe é filha de classe
class Pai:
    pass

class Filha(Pai):
    pass

class Neta(Filha):
    pass

# Retorna True ou False caso seja instância de um objeto
print(issubclass(Pai, Filha))
print(issubclass(Filha, Pai))
print(issubclass(Neta, Pai))

# Outro modo é usar o __bases__
# Porém informa somente qual é a superclasse direta 
print(Filha.__bases__)
print(Pai.__bases__)
print(Neta.__bases__)

# Verificando se algo pode ser instanciado
print(callable(Pai))
print(callable(object))
print(callable(5))
print(callable(bradesco)) # Vai retornar false pois a instância bradesco não é callable

# Podemos criar o __call__ em uma classe para tornar uma instância callable
class OutraConta(object):
    def __call__(self, texto):
        return texto

caixa = OutraConta()
print(callable(caixa))
print(caixa('Ola eu chamei o método especial __call__'))
