"""
# Descrição

Arquivo relacionado à atividade 5.5 da parte 1.

# Exercício

5.5 – Cores de alienígenas #3: Transforme sua cadeia if-else do Exercício 5.4
em uma cadeia if-elif-else.
• Se o alienígena for verde, mostre uma mensagem informando que o jogador
ganhou cinco pontos.
• Se o alienígena for amarelo, mostre uma mensagem informando que o
jogador ganhou dez pontos.
• Se o alienígena for vermelho, mostre uma mensagem informando que o
jogador ganhou quinze pontos.
• Escreva três versões desse programa, garantindo que cada mensagem seja
exibida para a cor apropriada do alienígena.

# Resposta

OK
"""

alien_color = "green"

if alien_color == "green":
    print("O jogador ganhou 5 pontos por atingir o alienígena.")
elif alien_color == "yellow":
    print("O jogador ganhou 10 pontos por atingir o alienígena.")
elif alien_color == "red":
    print("O jogador ganhou 15 pontos por atingir o alienígena.")
    