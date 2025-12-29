"""
# Descrição

Arquivo relacionado à atividade 4.5 da parte 1.

# Exercício

4.5 – Somando um milhão: Crie uma lista de números de um a um milhão e, em 
seguida, use min() e max() para garantir que sua lista realmente começa em 
um e termina em um milhão. Além disso, utilize a função sum() para ver a 
rapidez com que Python é capaz de somar um milhão de números.

# Resposta

OK
"""

um_milhao = range(1, 1_000_001)

print(min(um_milhao))
print(max(um_milhao))
print(sum(um_milhao))