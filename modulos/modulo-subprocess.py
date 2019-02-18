'''
subprocess - alternativa ao os.popen -> largado desde o python 2.6
subprocess.call - executa o comando, mais indicado usar do que o os.system
subprocess.check_call - checa a saída do comando e se houver erro levanta excessão
subprocess.check_output - devolve a saída do comando 
    subprocess.Popen(args, bufsize=0, stdin=None, stdout=None, stderr=None, preexec_fn=None, shell=False)
        args = sequencia de argumentos do programa
        shell = mesma regra de call
        preexec_fn = chama programa antes da execução
        std-out/in/err - direciona a saida da execução
'''

import subprocess, sys

print('''Listar um diretório
O argumento shell tem de ser true no windows para executar programas contruidos internamente como type, dir, etc
Um programa normal como python não possui a necessidade deste argumento
No unix, por outro lado, o shell = false (padrão) indica que o comando será executado pelo os.execvp
quando shell = True o comando é executado na própria linha de comando''')
if 'win' in sys.platform:
    subprocess.call(['dir'], shell=True)
else:
    subprocess.call(['ls', '-l'])
input()

print('')
print('Lendo um arquivo')
if 'win' in sys.platform:
    subprocess.call(['type', 'modulo-subprocess.py'], shell=True)
else:
    subprocess.call(['cat', 'modulo-subprocess.py'])
input()

print('')
print('Vamos ver a saída de um arquivo que não existe')
if 'win' in sys.platform:
    try:
        subprocess.call(['type', 'nao-existe.py'], shell=True)
    except Exception as e:
        print(e)
else:
    try:
        subprocess.call(['cat', 'nao-existe.py'])
    except Exception as e:
        print(e)
input()

print('')
print('Armazenando a saída de cat')
if 'win' in sys.platform:
    saida = subprocess.call(['type', 'modulo-subprocess.py'], shell=True)
else:
    saida = subprocess.call(['cat', 'modulo-subprocess.py'])
    print('Saida: ' + saida)

