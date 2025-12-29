"""
# Descrição

Arquivo relacionado à atividade 4.13 da parte 1.

# Exercício

4.13 – Buffet: Um restaurante do tipo buffet oferece apenas cinco tipos 
básicos de comida. Pense em cinco pratos simples e armazene-os em uma tupla.
• Use um laço for para exibir cada prato oferecido pelo restaurante.
• Tente modificar um dos itens e cerifique-se de que Python rejeita a mudança.
• O restaurante muda seu cardápio, substituindo dois dos itens com pratos
diferentes. Acrescente um bloco de código que reescreva a tupla e, em
seguida, use um laço for para exibir cada um dos itens do cardápio
revisado.

# Resposta

OK
"""

pratos = (
    "Filet Mignon", "X-Burguer", "X-Bacon", "Tortilla", "Crepe"
)

print(" Cardápio ".center(30, "="))
for prato in pratos:
    print(prato)

# pratos[0] = "X-Bacon" # TypeError

pratos = list(pratos)
pratos[0] = "X-Bacon"
pratos[4] = "X-Tudo"
pratos = tuple(pratos)

print(" Cardápio ".center(30, "="))
for prato in pratos:
    print(prato)