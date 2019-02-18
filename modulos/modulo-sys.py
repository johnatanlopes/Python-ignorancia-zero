#### Módulo sys #####
'''
plataform = devolve a plataforma de execução
path = lista com todas as pastas ligadas ao programa
exit([args]) = termina a execução de um programa
modules = todos os módulos carregados
exec_info = tupla que contem a última excessão levantada
argv - Recebe argumentos por linha de comando
'''

import sys

# Verificando qual S.O estamos utilizando
print(sys.platform)

if 'win' in sys.platform:
    print('Você esta utilizando o Windows')
else:
    print('Você não esta utilizando o Windows')

# Imprimindo o PATH do S.O
# A lista de pastas exibidas é onde o python procura os arquivos
print(sys.path)

# Também podemos adicionar caminhos de outras pastas com o sys.path
sys.path.append('C:\\Windows\\tmp')

# sys.exit() fecha o programa
# sys.exit()
# print('Não imprimiu')

# o sys.exit() pode receber argumentos = numeros inteiros

# Imprime os modulos que estão carregados no programa
print(sys.modules)

# sys.argv
print(sys.argv)
if len(sys.argv) == 2:
    print(sys.argv[1])

# O sys.exec_info retorna a última linha do erro
# É útil para obter compactado o erro obtido
try:
    raise IndexError
except:
    print(sys.exc_info())