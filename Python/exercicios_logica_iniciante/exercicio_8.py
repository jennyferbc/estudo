#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês.

valor_hora = int(input("Informe o valor da sua hora trabalhada: "))
quantidade_hora = int(input("Informe a quantidade de horas trabalhadas: "))

resultado = float(quantidade_hora * valor_hora)

print("Total a receber: {:.2f}".format(resultado))

