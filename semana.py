# 4. Desenvolver um programa que leia um número de 1 a 7 e exiba o dia da semana:
#    1 - 'Domingo'
#    2 - 'Segunda'
#    3 - 'Terça'
#    4 - 'Quarta'
#    5 - 'Quinta'
#    6 - 'Sexta'
#    7 - 'Sábado'
# Qualquer outro numero exibir: 'Opção inválida!'

#entrada
dia = int(input("Digite um número para ver o dia da semana: "))

#processamento e saída
if dia == 1:
    print("Hoje é domingo")
elif dia == 2:
    print("Hoje é segunda")
elif dia == 3:
    print("Hoje é terça")
elif dia == 4:
    print("Hoje é quarta")
elif dia == 5:
    print("Hoje é quinta")
elif dia == 6:
    print("Hoje é sexta")
elif dia == 7:
    print("Hoje é sábado")
else:
    print("Opção inválida!")

