# 6. Desenvolva um programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem formam um triângulo e se formarem exibir na tela se é equilátero, isósceles ou escaleno.

# Sabemos que:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes

#entrada
lado1 = int(input("Informe o primeiro lado: "))
lado2 = int(input("Informe o segundo lado :"))
lado3 = int(input("Informe o terceiro lado :"))

#processamento e saída
if lado1+lado2 > lado3 and lado2+lado3 > lado1 and lado3+lado1 > lado2:
    print("Os valores coincidem com um triângulo")
    if lado1 == lado2 == lado3:
        print("O triângulo é equilátero")
    elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
        print("O triângulo é isósceles")
    else:
        print("O triângulo é escaleno")
else:
    print("Os valores não coincidem com um triângulo")

