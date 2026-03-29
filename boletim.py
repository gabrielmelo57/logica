# 12. Desenvolva um programa que leia quatro notas bimestrais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média final. A atribuição de conceitos obedece à tabela abaixo:
#   Média de Aproveitamento  Conceito
#   Entre 9.0 e 10.0        A
#   Entre 7.5 e 8.9         B
#   Entre 6.0 e 7.4         C
#   Entre 4.0 e 5.9         D
#   Entre zero e 3.9        E
# O programa deve exibir na tela:
#   1. As quatro notas bimestrais,
#   2. A média final,
#   3. O conceito correspondente e,
#   4. A mensagem "APROVADO" ou "Reprovado" de acordo com a regra a seguir:
#      4.1. Se o conceito       for A, B ou C    exibir "APROVADO"
#      4.2. Senão se o conceito for D ou E       exibir "REPROVADO"

nota1 = float(input("Digite a primeira nota bimestral: "))
nota2 = float(input("Digite a segunda nota bimestral: "))
nota3 = float(input("Digite a terceira nota bimestral: "))
nota4 = float(input("Digite a quarta nota bimestral: "))
media = (nota1 + nota2 + nota3 + nota4) / 4
print("As quatro notas bimestrais são:", nota1, nota2, nota3, nota4)
print("A média final é:", media)
if media >= 9.0 and media <= 10.0:
    conceito = "A"
elif media >= 7.5 and media < 9.0:
    conceito = "B"  
elif media >= 6.0 and media < 7.5:
    conceito = "C" 
elif media >= 4.0 and media < 6.0:
    conceito = "D"
else:    conceito = "E"
print("O conceito correspondente é:", conceito)
if conceito == "A" or conceito == "B" or conceito == "C":
    print("APROVADO")
else:
    print("REPROVADO")