"""
# Descrição

Arquivo relacionado à atividade 3.6 da parte 1.

# Exercício

3.6 – Mais convidados: Você acabou de encontrar uma mesa de jantar maior,
portanto agora tem mais espaço disponível. Pense em mais três convidados
para o jantar.
• Comece com seu programa do Exercício 3.4 ou do Exercício 3.5. Acrescente
uma instrução print no final de seu programa informando às pessoas que
você encontrou uma mesa de jantar maior.
• Utilize insert() para adicionar um novo convidado no início de sua lista.
• Utilize insert() para adicionar um novo convidado no meio de sua lista.
• Utilize append() para adicionar um novo convidado no final de sua lista.
• Exiba um novo conjunto de mensagens de convite, uma para cada pessoa
que está em sua lista.

# Resposta

OK
"""

# START - Código do programa 3.5

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

# END - Código do programa 3.5

print("Rapaziada, encontrei uma mesa de jantar maior!!!")

lista_de_convidados.insert(0, "Bill Gates")
lista_de_convidados.insert(
    # Seleciona o centro se for par e um dos dois meios do centro se for 
    # ímpar.
    round(len(lista_de_convidados)/2), 
    "Ada Lovelace"
)
lista_de_convidados.append("Richard Stallman")

for convidado in lista_de_convidados:
    print(f"{convidado}, você está convidado para um jantar.")