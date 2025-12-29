# Resumo

Neste capítulo aprendemos a trabalhar de modo eficiente com os
elementos de uma lista. Vimos como percorrer uma lista usando um laço
for, como Python usa indentação para estruturar um programa e como
evitar alguns erros comuns de indentação. Aprendemos a criar listas
numéricas simples, além de conhecermos algumas operações que
podem ser realizadas em listas numéricas. Aprendemos a fatiar uma lista
para trabalhar com um subconjunto de itens e a copiar listas de modo
adequado usando uma fatia. Também conhecemos as tuplas, que
oferecem um nível de proteção a um conjunto de valores que não deve
ser alterado, e aprendemos a estilizar seu código cada vez mais
complexo para facilitar sua leitura.
No Capítulo 5 veremos como responder de forma apropriada a
diferentes condições usando instruções if. Aprenderemos a combinar
conjuntos relativamente complexos de testes condicionais para
responder de forma apropriada ao tipo de situação desejada ou oferecer
informações que você esteja procurando. Também aprenderemos a usar
instruções if enquanto percorremos uma lista para realizar ações
específicas com elementos selecionados de uma lista.

# Exercícios

4.1 – Pizzas: Pense em pelo menos três tipos de pizzas favoritas. Armazene os
nomes dessas pizzas e, então, utilize um laço for para exibir o nome de cada
pizza.
• Modifique seu laço for para mostrar uma frase usando o nome da pizza em
vez de exibir apenas o nome dela. Para cada pizza, você deve ter uma linha
na saída contendo uma frase simples como Gosto de pizza de pepperoni.
• Acrescente uma linha no final de seu programa, fora do laço for, que informe
quanto você gosta de pizza. A saída deve ser constituída de três ou mais
linhas sobre os tipos de pizza que você gosta e de uma frase adicional, por
exemplo, Eu realmente adoro pizza!

4.2 – Animais: Pense em pelo menos três animais diferentes que tenham uma
característica em comum. Armazene os nomes desses animais em uma lista e,
então, utilize um laço for para exibir o nome de cada animal.
• Modifique seu programa para exibir uma frase sobre cada animal, por
exemplo, Um cachorro seria um ótimo animal de estimação.
• Acrescente uma linha no final de seu programa informando o que esses
animais têm em comum. Você poderia exibir uma frase como Qualquer um
desses animais seria um ótimo animal de estimação!

4.3 – Contando até vinte: Use um laço for para exibir os números de 1 a 20,
incluindo-os.

4.4 – Um milhão: Crie uma lista de números de um a um milhão e, então, use um
laço for para exibir os números. (Se a saída estiver demorando demais,
interrompa pressionando CTRL-C ou feche a janela de saída.) 

4.5 – Somando um milhão: Crie uma lista de números de um a um milhão e, em 
seguida, use min() e max() para garantir que sua lista realmente começa em 
um e termina em um milhão. Além disso, utilize a função sum() para ver a 
rapidez com que Python é capaz de somar um milhão de números.

4.6 – Números ímpares: Use o terceiro argumento da função range() para criar
uma lista de números ímpares de 1 a 20. Utilize um laço for para exibir todos
os números.

4.7 – Três: Crie uma lista de múltiplos de 3, de 3 a 30. Use um laço for para
exibir os números de sua lista.

4.8 – Cubos: Um número elevado à terceira potência é chamado de cubo. Por
exemplo, o cubo de 2 é escrito como 2**3 em Python. Crie uma lista dos dez
primeiros cubos (isto é, o cubo de cada inteiro de 1 a 10), e utilize um laço 
for para exibir o valor de cada cubo.

4.9 – Comprehension de cubos: Use uma list comprehension para gerar uma lista
dos dez primeiros cubos.

4.10 – Fatias: Usando um dos programas que você escreveu neste capítulo,
acrescente várias linhas no final do programa que façam o seguinte: 
• Exiba a mensagem Os três primeiros itens da lista são: Em seguida, use 
uma fatia para exibir os três primeiros itens da lista desse programa.
• Exiba a mensagem Três itens do meio da lista são:. Use uma fatia para exibir
três itens do meio da lista.
• Exiba a mensagem Os três últimos itens da lista são:. Use uma fatia para
exibir os três últimos itens da lista.

4.11 – Minhas pizzas, suas pizzas: Comece com seu programa do Exercício 4.1
(página 97). Faça uma cópia da lista de pizzas e chame-a de friend_pizzas.
Então faça o seguinte: 
• Adicione uma nova pizza à lista original.
• Adicione uma pizza diferente à lista friend_pizzas.
• Prove que você tem duas listas diferentes. Exiba a mensagem Minhas pizzas
favoritas são:; em seguida, utilize um laço for para exibir a primeira lista.
Exiba a mensagem As pizzas favoritas de meu amigo são:; em seguida, utilize
um laço for para exibir a segunda lista. Certifique-se de que cada pizza
nova esteja armazenada na lista apropriada.

4.12 – Mais laços: Todas as versões de foods.py nesta seção evitaram usar
laços for para fazer exibições a fim de economizar espaço. Escolha uma
versão de foods.py e escreva dois laços for para exibir cada lista de comidas.

4.13 – Buffet: Um restaurante do tipo buffet oferece apenas cinco tipos 
básicos de comida. Pense em cinco pratos simples e armazene-os em uma tupla.
• Use um laço for para exibir cada prato oferecido pelo restaurante.
• Tente modificar um dos itens e cerifique-se de que Python rejeita a mudança.
• O restaurante muda seu cardápio, substituindo dois dos itens com pratos
diferentes. Acrescente um bloco de código que reescreva a tupla e, em
seguida, use um laço for para exibir cada um dos itens do cardápio
revisado.

4.14 – PEP 8: Observe o guia de estilo da PEP 8 original em
https://python.org/dev/peps/pep-0008/. Você não usará boa parte dele agora,
mas pode ser interessante dar uma olhada.

4.15 – Revisão de código: Escolha três programas que você escreveu neste
capítulo e modifique-os para que estejam de acordo com a PEP 8: 
• Use quatro espaços para cada nível de indentação. Configure seu editor de 
texto para inserir quatro espaços sempre que a tecla TAB for usada, caso 
ainda não tenha feito isso (consulte o Apêndice B para ver instruções sobre 
como fazê-lo).
• Use menos de 80 caracteres em cada linha e configure seu editor para que
mostre uma linha vertical na posição do caractere de número 80.
• Não use linhas em branco em demasia em seus arquivos de programa.

# Respostas

4.1. No arquivo ["pizzas.py"](./pizzas.py).

4.2. No arquivo ["animals.py"](./animals.py).

4.3. No arquivo ["counting_to_twenty.py"](./counting_to_twenty.py).

4.4. No arquivo ["a_million.py"](./a_million.py).

4.5. No arquivo ["adding_a_million.py"](./adding_a_million.py).

4.6. No arquivo ["odd_numbers.py"](./odd_numbers.py).

4.7. No arquivo ["three.py"](./three.py).

4.8. No arquivo ["cubes.py"](./cubes.py).

4.9. No arquivo ["cubes_comprehension.py"](./cubes_comprehension.py).

4.10. No arquivo ["slices.py"](./slices.py).

4.11. No arquivo ["my_pizzas_your_pizza.py"](./my_pizzas_your_pizza.py).

4.12. Na verdade, eu usei laços for para imprimir dados na tela.

4.13. No arquivo ["buffet.py"](./buffet.py).

4.14. Feito e vou continuar aprendendo a convenção enquanto reviso.

4.15. No VSCode, modifica-se settings.json para "editor.rules": [80]. Em 
configurações, para os 4 espaços da identação pelo TAB.