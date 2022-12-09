# Conversão de tipos

# Convertendo tipos
# Em alguns momentos é necessário converter o tipo de uma variável para manipular de forma diferente. Por exemplo:
# Variáveis do tipo string, que armazenam números e precisamos fazer alguma operação matématica com esse valor.

# Convertendo inteiro para ponto flutuante
preco = 10
print(preco)

preco = float(preco)
print(preco)

# Na divisão de um número inteiro por outro usando uma barra '/', retornar ponto flutuante.
preco = 10 / 2 
print(preco)

# Convertendo ponto flutuante para inteiro

preco = 10.30
print(preco)

preco = int(preco)
print(preco)

# Na divisão de um número inteiro por outro usando duas barras '//', retornar ponto flutuante.
preco = 10 // 2 
print(preco)

# Númerico para string

preco = 10.50
idade = 28

print(str(preco))
print(str(idade))

texto = f"idade {idade} preco {preco}"
print(texto)

# String para númerico

preco = "10.50"
idade = "28"

print(float(preco))
print(int(idade))

