#Variáveis e Constantes

# O que são variáveis e constantes?

# Variáveis
# Em linguagens de programação podemos definir valores que podem sofrer alterações no decorrer da execução do programa. Esses valores recebem o nome de variáveis, pois eles nascem com um valor e não necessariamente devem permanecer com o mesmo durante a execução do programa.

age = 23
name = 'Guilherme'
print(f'Meu nome é {name} e eu tenho {age} ano(s) de idade.')

idade, nome = (23, 'Guilherme')
print(f'Meu nome é {nome} e eu tenho {idade} ano(s) de idade.')

# Alterando os valores
# Perceba que não precisamos definir o tipo de dados da variável, o Python faz isso automaticamente para nós. Por isso não podemos simplesmente criar uma variável sem atribuir um valor. Para alterar o valor da variável basta fazer uma atribuição de um novo valor:

age = 28
name = 'Guilherme'
print(f'Meu nome é {name} e eu tenho {age} ano(s) de idade.')

idade, nome = (27, 'Giovanna')
print(f'Meu nome é {nome} e eu tenho {idade} ano(s) de idade.')

# Constantes
# Assim como as variáveis, constantes são utilizadas para armazenar valores. Uma constante nasce com um valor e permanece com ele até o final da execução do programa, ou seja, o valor é imutável.

# Python não tem constantes
# Não existe uma palavra reservada para informar ao interpretador que o valor é constante. Em algumas linguagens por exemplo: Java e C utilizamos final e const, respectivamente para declarar uma constante.
# Em Python usamos a convenção que diz ao programador que a variável é uma constante. Para fazer isso, você deve criar a variável com o nome todo em letras maíusculas:

ABS_PATH = '/home/guilherme/Documents/python_couse/'
DEBUG = True
STATES = [
    'SP',
    'RJ',
    'MG',
]
AMOUNT = 30.2

# Boas práticas

# O padrão de nomes deve ser snake case.
# Escolher nomes sugestivos.
# Nome de constantes todo em maiúsculo.

