"""
# Descrição

Arquivo relacionado à atividade 5.11 da parte 1.

# Exercício

5.11 – Números ordinais: Números ordinais indicam sua posição em uma lista,
por exemplo, 1st ou 2nd, em inglês. A maioria dos números ordinais nessa
língua termina com th, exceto 1, 2 e 3.
• Armazene os números de 1 a 9 em uma lista.
• Percorra a lista com um laço.
• Use uma cadeia if-elif-else no laço para exibir a terminação apropriada
para cada número ordinal. Sua saída deverá conter "1st 2nd 3rd 4th 5th
6th 7th 8th 9th", e cada resultado deve estar em uma linha separada.

# Resposta

OK
"""

lista = [i for i in range(1, 10)]

for i in lista:
    # Prefiro switch-case (match)
    if i == 1:
        print(f"{i}st", end=" ")
    elif i == 2:
        print(f"{i}nd", end=" ")
    elif i == 3:
        print(f"{i}rd", end=" ")
    else:
        print(f"{i}th", end=" ")