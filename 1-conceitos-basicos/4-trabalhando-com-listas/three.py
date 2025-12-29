"""
# Descrição

Arquivo relacionado à atividade 4.7 da parte 1.

# Exercício

4.7– Três: Crie uma lista de múltiplos de 3, de 3 a 30. Use um laço for para
exibir os números de sua lista.

# Resposta

OK
"""

# Múltiplos de 3: 3n, 3(n + 1) = 3n + 3, ... Portanto, soma-se 3 continuamente.
multiplos_de_3 = range(3, 31, 3)

for multiplo_de_3 in multiplos_de_3:
    print(multiplo_de_3)