# 8. Desenvolva um calculadora que receba dois números e efetue uma das seguintes operações aritméticas:

#    1 - Adição
#    2 - Subtração
#    3 - Multiplicação
#    4 - Divisão
#    5 - Potência
#    6 - Raiz quadrada
#    7 - Número par
#    8 - Número ímpar

print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Potência")
print("6 - Raiz quadrada")
print("7 - Número par")
print("8 - Número ímpar")

operacao = int(input("Escolha uma operação: "))
valor1 = float(input("Digite o primeiro número: "))
valor2 = float(input("Digite o segundo número: "))
if operacao == 1:
    calculo = valor1 + valor2
    print("O resultado é", calculo)
if operacao == 2:
    calculo = valor1 - valor2
    print("O resultado é", calculo)
if operacao == 3:
    calculo = valor1 * valor2
    print("O resultado é", calculo)
if operacao == 4:
    calculo = valor1 / valor2
    print("O resultado é", calculo)
if operacao == 5:
    calculo = valor1 ** valor2
    print("O resultado é", calculo)
if operacao == 6:
    calculo = valor1 ** 0.5
    calculo2 = valor2 ** 0.5
    print("O primeiro resultado é", calculo, "e o segundo é", calculo2)
if operacao == 7:
    if valor1 % 2 == 0:
        print("O primeiro número é par")
    else:
        print("O primeiro número é ímpar")
    if valor2 % 2 == 0:
        print("O segundo número é par")
    else:
        print("O segundo número é ímpar")
if operacao == 8:
    if valor1 % 2 == 1:
        print("O primeiro número é ímpar")
    else:
        print("O primeiro número é par")
    if valor2 % 2 == 1:
        print("O segundo número é ímpar")
    else:
        print("O segundo número é par")
else:
    print("Operação inválida")