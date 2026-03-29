# 2. Desenvolver um programa que leia o consumo de água para uma residência normal e exiba o valor (R$) da conta baseado nos seguintes cálculos:
# Se o consumo for menor ou igual a 10m3, então R$ 22,38
# Se o consumo for menor ou igual a 20m3, então R$ 3,50 por m3
# Se o consumo for menor ou igual a 50m3, então R$ 8,75 por m3
# Se o consumo for acima dos 50m3, então R$ 9,64 por m3

# Entrada
metros = float(input("Digite a quantidade de consumo em m3 (Metros Cúbicos): "))

#Processamento e saída
if metros <= 10:
    print("O consumo foi de R$ 22.38")
elif metros <= 20:
    print(f"O consumo foi de: R${metros * 3.50}")
elif metros <= 50:
    print(f"O consumo foi de: R${metros * 8.75}")
else:
    print(f"O consumo foi de: R${metros * 9.64}")

