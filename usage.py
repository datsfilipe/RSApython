# Esse .py vai te mostrar um tutorial de utilização do programa, como uma lista string.

def main():
    query = input('Você deseja começar este tutorial? / use s para sim e n para não!\n')
    if query == 's':
        print ("\n\nPara começar, veja a lista de comandos a seguir, são poucos e não tão difíceis, aqui está ela: \nPrimeiro comando- python keygen.py -pq primeiro-valor (1) segundo-valor (2) -x valor-desejado (3)\n\nExplicando:\n(1) - primeiro-valor = esse campo vai receber o primeiro valor de -pq, caso não queira inseri-lo, não há problema, pode esquecê-lo, pois eles tem valores pré-estabelecidos nesses casos.\n(2) - segundo-valor = da mesma forma que o primeiro, sem nenhuma surpresa, inseri-lo ou não vai do seu gosto.\n(3) - valor-desejado: esse valor é, também de inserção opcional, tendo como valor padrão 1.\n\nExemplos de uso:\npython keygen.py -pq 5077 907 -x 50 - EXEMPLO COM INSERÇÃO DE VALORES\npython keygen.py - EXEMPLO SEM INSERÇÃO DE VALORES\n")
        print ("Para começar, veja a lista de comandos a seguir, são poucos e não tão difíceis, aqui está ela: \nSegundo comando - python encryption.py -pq módulo de keygen (1) -m valor (2) --key chave-pública/privada (3)\n\nExplicando:\n(1) - módulo = esse campo vai receber o módulo de saída do keygen, nosso primeiro comando, basta copiá-lo e colar nessa área do comando.\n(2) - valor = aqui você adicionará o número inteiro que deseja criptografar ou descriptografar.\n(3) - chave-pública/chave-privada: para criptografia use a chave pública, para descriptografia use a privada. Ambas podem ser encontradas na saída do comando keygen.\n\nExemplos de uso:\npython encryption.py -pq 4604839 -m 20 --key 289\nObs: esse comando de encryption só pode ser executado a partir da inserção de valores!\n\nEspero que sua experiência utilizando a aplicação seja a melhor possível =)")
    elif query == 'n':
        print('Obrigado por usar o programa!')
        return
    else:
        raise ValueError('Não foi indicado um valor correto para a operação, por favor insira somente o que foi requisitado.')


main()