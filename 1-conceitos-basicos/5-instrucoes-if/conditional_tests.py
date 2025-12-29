"""
# Descrição

Arquivo relacionado à atividade 5.1 da parte 1.

# Exercício

5.1 – Testes condicionais: Escreva uma série de testes condicionais. Exiba uma
frase que descreva o teste e o resultado previsto para cada um. Seu código
deverá ser semelhante a: car = 'subaru'
print("Is car == 'subaru'? I predict True.") print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.") print(car == 'audi') 
• Observe atentamente seus resultados e certifique-se de que compreende
por que cada linha é avaliada como True ou False.
• Crie pelo menos dez testes. Tenha no mínimo cinco testes avaliados como
True e outros cinco avaliados como False.

# Resposta

OK
"""

nome = "Heitor"
idade = 18
altura = 1.8

print("Meu nome é Heitor?")
print(nome == "Heitor")

print("Minha idade é 18?")
print(idade == 18)

print("Minha altura é 1.8?")
print(altura == 1.8)

print("Meu nome é Heitor e minha altura não é 1.6?")
print(nome == "Heitor" and altura != 1.6)

print("Minha idade não é 16 e minha altura é 1.8?")
print(idade != 16 and altura == 1.8)

print("Meu nome é Carlos?")
print(nome == "Carlos")

print("Minha idade é 16?")
print(idade == 16)

print("Minha altura é 1.7?")
print(altura == 1.7)

print("Meu nome é João e minha altura não é 1.7?")
print(nome == "João" and altura != 1.7)

print("Minha idade é 16 e minha altura é 1.8?")
print(idade == 16 and altura == 1.8)