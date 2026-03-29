# 3. Desenvolver um programa que leia o consumo de água para prédios comerciais e industriais e exiba o valor (R$) da conta baseado nos seguintes cálculos:
# Se o consumo for menor ou igual a 10m3, então R$ 44,95
# Se o consumo for menor ou igual a 20m3, então R$ 8,75 por m3
# Se o consumo for menor ou igual a 50m3, então R$ 16,76 por m3
# Se o consumo for acima dos 50m3, então R$ 17,46 por m3

# Entrada
metros = float(input("Digite a quantidade de consumo em m3 (Metros Cúbicos): "))

#Processamento e saída
if metros <= 10:
    print("O consumo foi de R$ 44.95")
elif metros <= 20:
    print(f"O consumo foi de: R${metros * 8.75}")
elif metros <= 50:
    print(f"O consumo foi de: R${metros * 16.76}")
else:
    print(f"O consumo foi de: R${metros * 17.46}")

