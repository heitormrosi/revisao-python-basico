"""
# Descrição

Arquivo relacionado à atividade 6.5 da parte 1.

# Exercício

6.5 – Rios: Crie um dicionário que contenha três rios importantes e o país que
cada rio corta. Um par chave-valor poderia ser 'nilo': 'egito'.
• Use um laço para exibir uma frase sobre cada rio, por exemplo, O Nilo corre
pelo Egito.
• Use um laço para exibir o nome de cada rio incluído no dicionário.
• Use um laço para exibir o nome de cada país incluído no dicionário.

# Resposta

OK
"""

rios = {
    "nilo": "egito",
    "amarelo": "china",
    "gangis": "índia"
}

for k, v in rios.items():
    print(f"O rio {k.title()} corre pelo(a) {v.title()}")

for rio in rios.keys():
    print(rio.title())

for pais in rios.values():
    print(pais.title())