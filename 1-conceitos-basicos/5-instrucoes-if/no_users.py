"""
# Descrição

Arquivo relacionado à atividade 5.9 da parte 1.

# Exercício

5.9 – Sem usuários: Acrescente um teste if em hello_admin.py para garantir
que a lista de usuários não esteja vazia.
• Se a lista estiver vazia, mostre a mensagem Precisamos encontrar alguns
usuários!
• Remova todos os nomes de usuário de sua lista e certifique-se de que a
mensagem correta seja exibida.

# Resposta

OK
"""

users = [
    "heitor", "pc", "admin", "joao", "pineapple"
]

users = []

if not users:
    print("Precisamos encontrar alguns usuários!")
else:
    for user in users:
        if user == "admin":
            print("Olá, admin, gostaria de ver um relatório de status?")
        else:
            print(f"Olá, {user}, obrigado por fazer login novamente.")