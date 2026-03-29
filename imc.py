# 5. Desenvolver um programa que leia o peso e a altura de uma pessoa e calcule seu imc utilizando a fórmula: imc = peso / altura * altura
# Com o imc exiba para o usuário seu imc e a classificação:
# IMC		Classificação
# < 16		'Magreza grave'
# 16 a < 17	'Magreza moderada'
# 17 a < 18,5	'Magreza leve'
# 18,5 a < 25	'Saudável'
# 25 a < 30	'Sobrepeso'
# 30 a < 35	'Obesidade Grau I'
# 35 a < 40	'Obesidade Grau II (severa)'
# ≥ 40		'Obesidade Grau III (mórbida)'

#entrada
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite seu altura em metros: "))

#processamento
imc = peso/altura**2

#processamento e saída
if imc < 16:
    print("Você tem magreza grave")
elif imc >= 16 and imc <17:
    print("Você tem magreza moderada")
elif imc >= 17 and imc <18.5:
    print("Você tem magreza leve")
elif imc >= 18.5 and imc <25:
    print("Você está saudável")
elif imc >= 25 and imc <30:
    print("Você tem sobrepeso")
elif imc >= 30 and imc <35:
    print("Você tem obesidade grau I")
elif imc >= 35 and imc <40:
    print("Você tem obesidade grau II (severa)")
else:
    print("Você tem obesidade grau III (mórbida)")

