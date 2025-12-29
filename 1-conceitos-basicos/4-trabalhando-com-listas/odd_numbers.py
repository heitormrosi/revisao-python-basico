"""
# Descrição

Arquivo relacionado à atividade 4.6 da parte 1.

# Exercício

4.6 – Números ímpares: Use o terceiro argumento da função range() para criar
uma lista de números ímpares de 1 a 20. Utilize um laço for para exibir todos
os números.

# Resposta

OK
"""

# Como os ímpares são 2n + 1 e já tenho 1, é só continuamente somar 2.
impares = range(1, 21, 2)

for impar in impares:
    print(impar)