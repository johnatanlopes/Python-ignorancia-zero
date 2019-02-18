"""
os.path
isdir = é diretório?
isfile = é arquivo?
exists = existe diretório/arquivo?
getsize = obtem o tamanho do arquivo/diretório
split = separa caminho do arquivo numa string (pode receber lista ou tupla também)
join = junta caminho com arquivo
dirname = obtem diretório da string
basename = obtem arquivo da string
splitext = obtem extensão do arquivo
normpath = obtem caminho com separador adequado
abspath = retorna o diretório do caminho especificado
 
PhotoImage(file = os.path.join("Imagens","mario.pgm"))
"""
 
import os
 
caminho = os.getcwd() + os.sep + 'modulo-os-path.py'
 
print('os.path.isdir("ex") = ', os.path.isdir('ex'))
print('os.path.isfile("ex") = ', os.path.isfile('ex'))
print('os.path.exists("ex") = ', os.path.exists('ex'))
print('os.path.exists("modulo-os-path.py") = ', os.path.exists('modulo-os-path.py'))
print('os.path.getsize("modulo-os-path.py") = ', os.path.getsize('modulo-os-path.py'))
print('os.path.split("%s") = ' % caminho, os.path.split(caminho))
print('os.path.join("media", "modulo-os-path.py") = ', os.path.join("media", "modulo-os-path.py"))
print('os.path.join("media", "modulo-os-path.py", "HD") = ', os.path.join("media", "modulo-os-path.py", 'HD'))
print('os.path.dirname("%s") = ' % caminho, os.path.dirname(caminho))
print('os.path.basename("%s") = ' % caminho, os.path.basename(caminho))
print('os.path.splitext("modulo-os-path.py") = ', os.path.splitext("modulo-os-path.py"))
print('os.path.normpath("media\\pedro\\HD\\Aulas/iz/aulas_python/modulo-os-path/modulo-os-path.py") = ', os.path.normpath("media\\pedro\\HD\\Aulas/iz/aulas_python/107/107.py"))
print('os.path.abspath("") = ', os.path.abspath(""))
print('os.path.abspath("ex") = ', os.path.abspath("ex"))
print('os.path.abspath("%s")' % os.curdir, os.path.abspath("."))
print('os.path.abspath("%s")' % os.pardir, os.path.abspath(".."))