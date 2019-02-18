"""
system = permite executar um comando
popen = permite inserir comandos mas direcionar sua saída
startfile = abre arquivo no programa default
"""

import os

# type para ler no windows
# cat para ler no linux
os.system('type modulo-os-shell-commands.py')
print(os.system('type modulo-os-shell-commands.py')) # Retorna o valor da execução 0 para sucesso

# Listando os conteudos do diretório
os.system('dir %s' % os.getcwd())
print(os.system('dir x')) # Retornou 1 já que a pasta não foi encontrada

# Com os.popen pode ler saidas de arquivos
os.popen('type modulo-os-shell-commands.py').read()

# Ler linhas de diretórios
os.popen('dir %s' % os.getcwd()).readlines()

# abre arquivos no windows
os.startfile('ex' + os.sep + 'sons' + os.sep + 'som_text.wav')


