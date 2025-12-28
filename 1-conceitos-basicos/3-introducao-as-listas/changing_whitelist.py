"""
# Descrição

Arquivo relacionado à atividade 3.5 da parte 1.

# Exercício

3.5 – Alterando a lista de convidados: Você acabou de saber que um de seus
convidados não poderá comparecer ao jantar, portanto será necessário enviar
um novo conjunto de convites. Você deverá pensar em outra pessoa para
convidar.
• Comece com seu programa do Exercício 3.4. Acrescente uma instrução print
no final de seu programa, especificando o nome do convidado que não
poderá comparecer.
• Modifique sua lista, substituindo o nome do convidado que não poderá
comparecer pelo nome da nova pessoa que você está convidando.
• Exiba um segundo conjunto de mensagens com o convite, uma para cada
pessoa que continua presente em sua lista.

# Resposta

OK
"""

lista_de_convidados = [
    "Albert Einstein", "César Lattes", "Edward Snowden", "Alan Turing"
]

# Mostra a lista de convidados.
for convidado in lista_de_convidados:
    print(f"{convidado}, você está convidado para um jantar.")


print("Alan Turing não poderá comparecer.")
# Substitui o convidado ausente por outro.
index_convidado_ausente = lista_de_convidados.index("Alan Turing")
lista_de_convidados[index_convidado_ausente] = "Linus Torvalds"

for convidado in lista_de_convidados:
    print(f"{convidado}, você está convidado para um jantar.")