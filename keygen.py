import math
import sys

# Aqui verificamos se os valores são números primos !
# n na função será p e q durante a execução do programa.

def isPrime (n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

# Abaixo utilizamos da biblioteca sys para determinar flags para o comando da nossa aplicação no terminal.

# >>python keygen.py -pq 2 3 -x 1
# >>sys.argv -> [keygen.py, -pq, 2, 3, -x, 1]


# Procuramos o valor da variável -pq nas flags do comando, caso não seja encontrado, ela recebe os valores pré setados.

if '-pq' in sys.argv:
    flag_index = sys.argv.index('-pq')
    flag_index += 1
    p = int(sys.argv[flag_index]) # Os valores vêm como string, por isso a necessidade de transformá-los em int.
    flag_index += 1
    q = int(sys.argv[flag_index])
else:
    p = 1009
    q = 2741

# Testamos se os valores são primos.

if not isPrime(p) or not isPrime(q):
    raise ValueError('P ou Q não é um número primo')

# Procuramos a variável -x nas flags, caso não encontre ela recebe o valor pré setado 1.

if '-x' in sys.argv:
    flag_index = sys.argv.index('-x')
    flag_index += 1
    x = int(sys.argv[flag_index])
else:
    x = 1

# Esta variável representa o valor que xy deve ter.

eq = (p - 1) * (q - 1) + 1

y = 1
xy = x * y # Caso atinja o valor almejado, o programa não entra no while.

# O fato de x * y não ser sempre igual a eq se dá pois eq / x nem sempre dá um resultado inteiro e quando isso acontece ele é arredondado. Por isso executaremos um while até x * y ser igual a eq, afinal nem sempre essa condição é atendida trabalhando com números inteiros.

while xy != eq:
    x += 1
    y = eq // x
    xy = x * y

# Mostrando os resultados.

print ("Chave pública, x: " + str(x))
print ("Chave privada, y: " + str(y))
print ("Módulo (pq): " + str (p * q))