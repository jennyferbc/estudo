#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, 
# utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

altura = float(input("Informe sua altura: "))
sexo = input("Informe F para o sexo Feminino ou M para Masculino: ")

peso_ideal_F = (62.1 * altura) - 44.7
peso_ideal_M = (72.7 * altura) - 58

if(sexo == "F"):
    print(peso_ideal_F)
else:
    print(peso_ideal_M)