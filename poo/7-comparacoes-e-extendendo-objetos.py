class Conta(object):
    def __init__(self, id, saldo):
        self.id = id
        self.saldo = saldo

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor

    def __le__(self, outraInstancia):
        if self.id <= outraInstancia.id:
            return True
        else:
            return False

    def __eq__(self, outraInstancia):
        if self.id == outraInstancia.id:
            return True
        else:
            return False

    def __ge__(self, outraInstancia):
        if self.id >= outraInstancia.id:
            return True
        else:
            return False

    def __lt__(self, outraInstancia):
        if self.id < outraInstancia.id:
            return True
        else:
            return False

    def __gt__(self, outraInstancia):
        if self.id > outraInstancia.id:
            return True
        else:
            return False

    def __ne__(self, outraInstancia):
        if self.id != outraInstancia.id:
            return True
        else:
            return False

itau = Conta(123, 4000)
bradesco = Conta(123, 5000)

# Objetos apontam para uma referência, quando criamos um objeto recebemos uma referência única
# Então esses dois objetos são diferentes
print(itau == bradesco)

# Objetos diferentes não são iguais mesmo tendo valores iguais
itau2 = Conta(123, 4000)
print(itau == itau2)

itau3 = itau
itau3.deposita(15)
print(itau.saldo)

# Quando associamos itau a itau3 estamos fazendo um apontamento, então retorna true a verificação abaixo,
# já que estão apontando para o mesmo endereço em memória
print(itau == itau3)

# Verificando se armazenam o mesmo objeto de outra forma:
# Utilizando o método id()
print(id(itau))
print(id(itau2))
print(id(itau3))

# Métodos de comparação para utilizar em objetos, retorna um boolean
# __le__ x <= y, __eq__ x == y, __ge__ x >= y, __ly__ x < y, __gt__ x > y, __ne__ !=

print(itau == itau2)
print(itau <= itau2)
print(itau <= itau3)
print(itau <= bradesco)


# Rescrevendo o método sort para ordenar uma lista de contas
class Contas(list):
    def sort(self):
        copia = self.copy()
        tam = len(self)
        self.clear()
        while len(self) < tam:
            min_id = copia[0]
            for conta in copia:
                if conta.id < min_id.id:
                    min_id = conta
            self.append(min_id)
            copia.remove(min_id)

# Extendendo objetos
class Banco(object):
    def __init__(self):
        self.contas = Contas()

itau = Conta(141,2323)
santander = Conta(5658, 1000)
caixa = Conta(123, 1569)

banco = Banco()
banco.contas.append(itau)
banco.contas.append(caixa)
banco.contas.append(santander)
banco.contas.sort()
print(banco.contas)
print(banco.contas[0].id)