"""
# Descrição

Arquivo relacionado à atividade 6.1 da parte 1.

# Exercício

6.1 – Pessoa: Use um dicionário para armazenar informações sobre uma pessoa
que você conheça. Armazene seu primeiro nome, o sobrenome, a idade e a
cidade em que ela vive. Você deverá ter chaves como first_name, last_name,
age e city. Mostre cada informação armazenada em seu dicionário.

# Resposta

OK
"""

pessoa = {}

# Prefiro utilizar .setdefault() e .get() ao invés de acessar com [].

pessoa["first_name"] = "Heitor"
pessoa["last_name"] = "Rosi"
pessoa["age"] = 18
pessoa["city"] = "Serra"

for k, v in pessoa.items():
    print(k + ": " + str(v))