# Podemos utilizar o % em variáveis
# o %i é utilizado em inteiros
x = 'Eu tenho %i anos' % 10
print(x)

# Podemos utilizar direto no print
print('Eu tenho %i anos' % 10)

# Numeros float
print('Eu tenho R$ %.2f reais' % 10.1899)

# Adicionando variaveis dentro de strings com %s
nome = input("Digite seu nome: ")
x = "Ola %s, seja bem0vindo ao nosso programa" % (nome)
print(x)

# Utilizando o end no print:
# Com o end no print ele adiciona cada print na mesma linha
print('Ola', end=' ')
print('Meu', end=' ')
print('Nome', end=' ')
print('é', end=' ')
print('Johnatan', end=' ')
print('')

for i in range(1, 21):
    print(i, end=' ')