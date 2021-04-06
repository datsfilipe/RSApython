import sys

# Uma função para fisgar todos os argumentos (flags) passados na execução do comando.

def extractInfo(flag):
    i = sys.argv.index(flag) + 1
    return sys.argv[i]

# Uma série de casos para verificar se as flags estão presentes no comando.

if '-pq' not in sys.argv:
    print ('Você precisa informar PQ utilizando a flag -pq')
    sys.exit(1)

if '--key' not in sys.argv:
    print ('Você deve informar a sua chave utilizando a flag --key')
    sys.exit(1)

if '-m' not in sys.argv:
    print ('Você deve informar a mensagem utilizando a flag -m')

# Atribuindo o valor das variáveis com as flags do comando, a partir da função extractInfo().

pq = int(extractInfo('-pq'))
key = int(extractInfo('--key'))
m = int(extractInfo('-m'))

# Processo de encripitação e descripitação da mensagem usando a chave passada pelo comando.

# Obs: a mensagem tem que ser um número, o programa não trabalha com strings ou outros tipos de variável.

exp = m ** key
processedMessage = exp % pq

# Exibição do resultado, mensagem processada com sucesso.

print ('Sua mensagem criptografada/descriptografada é: ' + str(processedMessage))