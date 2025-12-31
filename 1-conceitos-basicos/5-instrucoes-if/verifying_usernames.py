"""
# Descrição

Arquivo relacionado à atividade 5.10 da parte 1.

# Exercício

5.10 – Verificando nomes de usuários: Faça o seguinte para criar um programa
que simule o modo como os sites garantem que todos tenham um nome de
usuário único.
• Crie uma lista chamada current_users com cinco ou mais nomes de usuários.
• Crie outra lista chamada new_users com cinco nomes de usuários. Garanta
que um ou dois dos novos usuários também estejam na lista current_users.
• Percorra a lista new_users com um laço para ver se cada novo nome de
usuário já foi usado. Em caso afirmativo, mostre uma mensagem informando
que a pessoa deverá fornecer um novo nome. Se um nome de usuário não foi
usado, apresente uma mensagem dizendo que o nome do usuário está
disponível.
• Certifique-se de que sua comparação não levará em conta as diferenças
entre letras maiúsculas e minúsculas. Se 'John' foi usado, 'JOHN' não deverá
ser aceito.

# Resposta

OK
"""

current_users = ['ana', 'bruno', 'carla', 'diego', 'elena', 'fabio']
new_users = ['carla', 'gabriel', 'HELENA', 'diego', 'lucas']

# O(n^2)
for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"{new_user} já existe. Forneça um novo nome de usuário.")
    else:
        print(f"O nome de usuário {new_user} está disponível.")