# 9 - Desenvolva um programa que leia o valor (R$) de um salário qualquer e calcule e exiba o desconto com IRRF e INSS;
# O desconto do IRRF é de 27,5% para salários acima de R$ 4.664,68, 15% para salários entre R$ 1.903,99 e R$ 4.664,68 e isento para salários abaixo de R$ 1.903,99;
# O desconto do INSS é de 11% para salários acima de R$ 1.100,00 e 7,5% para salários entre R$ 1.100,00 e R$ 2.203,48 e isento para salários abaixo de R$ 1.100,00.

salario = float(input("Digite o valor do salário: "))
if salario > 4664.68:
    irrf = salario * 0.275
    print("O desconto do IRRF é de R$", irrf)
elif salario > 1903.99:
    irrf = salario * 0.15
    print("O desconto do IRRF é de R$", irrf)
else:
    irrf = 0
    print("O desconto do IRRF é de R$", irrf)

if salario > 2203.48:
    inss = salario * 0.11
    print("O desconto do INSS é de R$", inss)
elif salario > 1100.00:
    inss = salario * 0.075
    print("O desconto do INSS é de R$", inss)
else:
    inss = 0
    print("O desconto do INSS é de R$", inss)
desconto = salario - irrf - inss
print("O salário líquido é de R$", desconto)