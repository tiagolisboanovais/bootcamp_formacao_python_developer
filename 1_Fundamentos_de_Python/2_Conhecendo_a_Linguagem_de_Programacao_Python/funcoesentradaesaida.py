# Funções de entrada e saída
# Aprender como receber e exibir informações para o usuário

# Lendo valores com a função input
# A função builtin input é utilizada quando queremos ler dados da entrada padrão (teclado). Ela recebe um argumento do tipo string, que é exibido para o usuário na saída padrão (tela). A função lê a entrada, converte para string e retorna valor.

nome = input("Informe o seu nome: ")
sobrenome = input("Informe o seu sobrenome: ")

# Função Print
# A função builtin print é utilizada quando queremos exibir dados na saída padrão (tela). Ela receber argumento obrigatório do tipo varargs de objetos e 4 argumentos opcionais (sep, end, file e flush). Todos os objetos são convertidos para string, separados por sep e terminados por end. A string final é exibida para o usuário.

# Por padrão o 'sep' é um espaço vazio, o 'end' é uma quebra de linha.

print(nome)
print(sobrenome)
print(nome, sobrenome)
print(nome, sobrenome, end='...\n')
print(nome, sobrenome, sep='#')
