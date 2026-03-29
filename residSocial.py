# 1. Desenvolver um programa que leia o consumo de água para uma residência social e exiba o valor (R$) da conta baseado nos seguintes cálculos:
# Se o consumo for menor ou igual a 10m3, então R$ 7,59
# Se o consumo for menor ou igual a 20m3, então R$ 1,31 por m3
# Se o consumo for menor ou igual a 30m3, então R$ 4,64 por m3
# Se o consumo for menor ou igual a 50m3, então R$ 6,62 por m3
# Se o consumo for acima dos 50m3, então R$ 7,31 por m3

# Entrada
metros = float(input("Digite a quantidade de consumo em m3 (Metros Cúbicos): "))

#Processamento e saída
if metros <= 10:
    print("O consumo foi de R$ 7.49")
elif metros <= 20:
    print(f"O consumo foi de: R${metros * 1.31}")
elif metros <= 30:
    print(f"O consumo foi de: R${metros * 4.64}")
elif metros <= 50:
    print(f"O consumo foi de: R${metros * 6.62}")
else:
    print(f"O consumo foi de: R${metros * 7.31}")

