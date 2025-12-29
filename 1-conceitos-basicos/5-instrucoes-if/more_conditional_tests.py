"""
# Descrição

Arquivo relacionado à atividade 5.2 da parte 1.

# Exercício

5.2 – Mais testes condicionais: Você não precisa limitar o número de testes que
criar em dez. Se quiser testar mais comparações, escreva outros testes e
acrescente-os em conditional_tests.py. Tenha pelo menos um resultado True e um
False para cada um dos casos a seguir: 
• testes de igualdade e de não igualdade com strings; 
• testes usando a função lower(); 
• testes numéricos que envolvam igualdade e não igualdade, maior e menor que, 
maior ou igual a e menor ou igual a; 
• testes usando as palavras reservadas and e or; 
• testes para verificar se um item está em uma lista; 
• testes para verificar se um item não está em uma lista.

# Resposta

OK
"""

# START - Código do programa 5.1

idades = [
    1, 2, 18, 20, 21
]

nomes = [
    "João", "Paulo", "Pedro", "Carlos"
]

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

# END - Código do programa 5.1

print("Meu nome é Pedro?")
print(nome.lower() == "pedro")

print("Sou mais alto ou tenho 1.8 de altura?")
print(altura >= 1.8)

print("Sou mais alto que 1.9?")
print(altura > 1.9)

print("Minha idade é menor ou igual a 18?")
print(idade <= 18)

print("Sou mais jovem que 40 anos?")
print(idade < 40)

print("Meu nome é Heitor ou tenho 20 anos?")
print(nome == "Heitor" or idade == 20)

print("Minha idade está na lista de idades?")
print(idade in idades)

print("Meu nome não está na lista de nomes?")
print(nome not in nomes)