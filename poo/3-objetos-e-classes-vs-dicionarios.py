# Dicionario
pessoa = {'Nome': 'Lucas', 'Emprego': 'Advogado', 'Idade': 20, 'Cor de cabelo': 'Preto'}

# Pode alterar valores no dicionario
pessoa['nome'] = 'João'

# Exibir valores das chaves
print(pessoa['Emprego'])

# Criar chaves novos e acessa-las
pessoa['Peso'] = 105
print(pessoa['Peso'])

# Facilicando a criação de um dicionário
dic = dict(nome = 'Joao', emprego = 'Advogado', idade = 20)


'''
Com objetos podemos ter construtor, herança, métodos, encapsulamento, atributos, associações já os dicionários não
'''
# Criando nossa classe
class PessoaObj(object):
    # Utilizamos pass para criar uma classe vazia
    pass

Johnatan = PessoaObj()
Johnatan.nome = 'Johnatan'
Johnatan.emprego = 'Advogado'
Johnatan.corDeCabelo = 'Preto'

# Imprimindo a classe como dicionario com método especial __dict__
print(Johnatan.__dict__)
