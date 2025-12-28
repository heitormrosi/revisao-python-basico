"""
# Descrição

Arquivo relacionado à atividade 3.10 da parte 1.

# Exercício

3.10 – Todas as funções: Pensa em algo que você poderia armazenar em uma
lista. Por exemplo, você poderia criar uma lista de montanhas, rios, países,
cidades, idiomas ou qualquer outro item que quiser. Escreva um programa que
crie uma lista contendo esses itens e então utilize cada função apresentada
neste capítulo pelo menos uma vez.

# Resposta

OK
"""

itens_culturais = [
    "Tóquio",
    "Italiano",
    "Sushi",
    "Machu Picchu",
    "Francês",
    "Tacos",
    "Aurora Boreal",
    "Mandarim",
    "Feijoada",
    "Roma"
]

print(sorted(itens_culturais))
print(len(itens_culturais))
print(sorted(itens_culturais, reverse=True))
itens_culturais.sort()
print(itens_culturais)
itens_culturais.reverse()
print(itens_culturais)
itens_culturais.sort(reverse=True)
print(itens_culturais)

itens_culturais.append("Português")
itens_culturais.insert(0, "Acarajé")
del itens_culturais[4]
print(itens_culturais)

item1 = itens_culturais.pop()
item2 = itens_culturais.pop()

print(item1, item2)