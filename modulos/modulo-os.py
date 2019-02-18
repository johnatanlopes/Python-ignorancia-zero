#### Modulo os ####
'''
getpid - ID do processo que esta executando
getcwd - Recebe o diretório de trabalho atual
remove - Remove um arquivo
rename - renomeia um arquivo
urandom(n) - Retorna n bytes de criptografia fortemente de um dado aleatorio

CONSTANTES
    pathsep - separador de caminhos
    sep - separador de diretorios
    pardid - caminho de volta para do diretorio
    curdir - codigo para obter diretorio atual
    linesep - separador de linhas
    environ - dicionario com caminhos e configurações especificas do sistema
'''

import os, sys

# ID do programa e o diretório de trabalho
print(os.getpid(), os.getcwd())

# Renomar arquivo
# os.rename('arquivo', 'novoNome')

# Deletar o arquivo
# os.remove('novoArquivo')

# Gerando uma string aleatória e criptografada
print(os.urandom(5))

# Constantes especiais para diretórios
x = os.pathsep, os.sep, os.pardir, os.curdir, os.linesep
print(x)

# Dicionário com as configurações do sistema
print(list(os.environ.keys()))

# Valor de uma das chaves do dicionario
if 'win' in sys.platform:
    print(os.environ['TEMP'])

# Modificando os valores da chave
os.environ['USER'] = 'johnatan'
print(os.environ['USER'])