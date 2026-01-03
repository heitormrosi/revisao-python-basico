"""
# Descrição

Arquivo relacionado à atividade 6.4 da parte 1.

# Exercício

6.4 – Glossário 2: Agora que você já sabe como percorrer um dicionário com
um laço, limpe o código do Exercício 6.3 (página 148), substituindo sua
sequência de instruções print por um laço que percorra as chaves e os valores
do dicionário. Quando tiver certeza de que seu laço funciona, acrescente mais
cinco termos de Python ao seu glossário. Ao executar seu programa novamente,
essas palavras e significados novos deverão ser automaticamente incluídos na
saída.

# Resposta

OK
"""

glossario = {
    "lista": "Agrupamento de itens.",
    "laço": "Bloco de repetição.",
    "print": "Imprimir em inglês.",
    "for": "Para em inglês.",
    "zen": "Escola do budismo.",
    "if": "Se em inglês.",
    "else": "Senão em inglês",
    "elif": "Mistura de Se e Senão em inglês.",
    "condicional": "Que possui condição.",
    "variável": "Etiqueta para espaço de memória."
}

# Não precisei mudar.
for k, v in glossario.items():
    print(k + ":", end="\n\t")
    print(v)
