"""
# Descrição

Arquivo relacionado à atividade 3.7 da parte 1.

# Exercício

3.7 – Reduzindo a lista de convidados: Você acabou de descobrir que sua nova
mesa de jantar não chegará a tempo para o jantar e tem espaço para somente
dois convidados.
• Comece com seu programa do Exercício 3.6. Acrescente uma nova linha que
mostre uma mensagem informando que você pode convidar apenas duas
pessoas para o jantar.
• Utilize pop() para remover os convidados de sua lista, um de cada vez, até
que apenas dois nomes permaneçam em sua lista. Sempre que remover um
nome de sua lista, mostre uma mensagem a essa pessoa, permitindo que ela
saiba que você sente muito por não poder convidá-la para o jantar.
• Apresente uma mensagem para cada uma das duas pessoas que continuam
na lista, permitindo que elas saibam que ainda estão convidadas.
• Utilize del para remover os dois últimos nomes de sua lista, de modo que 
você tenha uma lista vazia. Mostre sua lista para garantir que você realmente 
tem uma lista vazia no final de seu programa.

# Resposta

OK
"""

# START - Código do programa 3.6

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

# Insere os novos convidados.
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

# END - Código do programa 3.7

print("Agora, só posso convidar duas pessoas para o jantar.")

# Remove os convidados até que sobrem apenas dois.
while len(lista_de_convidados) > 2:
    desconvidado = lista_de_convidados.pop()
    print(
        f"Me desculpe, {desconvidado}, por não poder te convidar para o jantar."
    )

for convidado in lista_de_convidados:
    print(f"{convidado}, você está convidado para um jantar.")

del lista_de_convidados[1]
del lista_de_convidados[0]

print(lista_de_convidados)