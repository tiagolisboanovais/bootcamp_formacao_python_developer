#Tipos de dados simples

letra = str(1)
num_int = int("1")
num_float = float ("1")
soma_bool = bool('1 + 1 == 2')

print(letra)
print(num_int)
print(num_float)
print(soma_bool)

# Modo Interativo

# Para acessar o programa em modo interativo basta colocar a flag -i, nesta sintax 'python -i nomeprograma.py'

# Dir - Sem argumentos, retorna a lista de nomes no escopo local atual. Com um argumento, retorna uma lista de atributos válidos para o objeto. Exemplo:

print(dir())
print(dir(100))

# Help - Invoca o sistema de ajuda integrado. É possível fazer buscas em modo interativo ou informar por parâmetro qual o nome do módulo, função, classe, método ou variável. Exemplo:
# Para sair help = enter, para sair da documentação = q
# Como se fosse documentação offline
# Mais informações: https://wiki.python.org.br/ModoInterativo

print(help())
print(help(100))



