"""
# Descrição

Arquivo relacionado à atividade 3.2 da parte 1.

# Exercício

3.2 – Saudações: Comece com a lista usada no Exercício 3.1, mas em vez de
simplesmente exibir o nome de cada pessoa, apresente uma mensagem a elas.
O texto de cada mensagem deve ser o mesmo, porém cada mensagem deve
estar personalizada com o nome da pessoa.

# Resposta

OK
"""

nomes = [
    "Danilo", "Natã", "Lorran"
]

mensagem = "Olá, {0}!"

print(mensagem.format(nomes[0]))
print(mensagem.format(nomes[1]))
print(mensagem.format(nomes[2]))