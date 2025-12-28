"""
# Descrição

Atividade relacionada à atividade 3.4 da parte 1.

# Exercício

3.4 – Lista de convidados: Se pudesse convidar alguém, vivo ou morto, para o 
jantar, quem você convidaria? Crie uma lista que inclua pelo menos três 
pessoas que você gostaria de convidar para jantar. Em seguida, utilize sua 
lista para exibir uma mensagem para cada pessoa, convidando-a para jantar.

# Resposta

OK
"""

lista_de_convidados = [
    "Albert Einstein", "César Lattes", "Edward Snowden", "Alan Turing"
]

for convidado in lista_de_convidados:
    print(f"{convidado}, você está convidado para um jantar.")