"""
# Descrição

Arquivo relacionado à atividade 3.11 da parte 1.

# Exercício

3.11 – Erro proposital: Se você ainda não recebeu um erro de índice em um de
seus programas, tente fazer um erro desse tipo acontecer. Altere um índice em
um de seus programas de modo a gerar um erro de índice. Não se esqueça de
corrigir o erro antes de fechar o programa.

# Resposta

OK, vou introduzir o erro em 3.2.
"""

nomes = [
    "Danilo", "Natã", "Lorran"
]

mensagem = "Olá, {0}!"

print(mensagem.format(nomes[0]))
print(mensagem.format(nomes[4])) # IndexError
print(mensagem.format(nomes[5])) # IndexError