"""
# Descrição

Arquivo relacionado à atividade 6.2 da parte 1.

# Exercício

6.2 – Números favoritos: Use um dicionário para armazenar os números favoritos
de algumas pessoas. Pense em cinco nomes e use-os como chaves em seu
dicionário. Pense em um número favorito para cada pessoa e armazene cada
um como um valor em seu dicionário. Exiba o nome de cada pessoa e seu
número favorito. Para que seja mais divertido ainda, faça uma enquete com
alguns amigos e obtenha alguns dados reais para o seu programa.

# Resposta

OK
"""

# Preguiça de pegar dados reais
numeros_favoritos = {
    "Carlos": 1,
    "Maria": 2,
    "João": 3,
    "André": 6,
    "Pedro": 9
}

print(" Números favoritos ".center(30, "="))
for k, v in numeros_favoritos.items():
    print(k + " -> " + str(v))