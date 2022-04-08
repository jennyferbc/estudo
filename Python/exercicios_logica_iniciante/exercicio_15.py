#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#a. salário bruto.
#b. quanto pagou ao INSS.
#c. quanto pagou ao sindicato.
#d. o salário líquido.
#e. calcule os descontos e o salário líquido, conforme a tabela abaixo:
#f. + Salário Bruto : R$
#g. - IR (11%) : R$
#h. - INSS (8%) : R$
#i. - Sindicato ( 5%) : R$
#j. = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.


ganho_por_hora = float(input("Informe o valor da hora trabalhada: "))
horas_trabalhadas_no_mes = float(input("Informe a quantidade de horas trabalhadas no mês: "))

salario_bruto = ganho_por_hora * horas_trabalhadas_no_mes
valor_inss = salario_bruto * 0.08
valor_sindicato = salario_bruto * 0.05
valor_ir = salario_bruto * 0.11

descontos = valor_inss + valor_sindicato + valor_ir
salario_liquido = salario_bruto - descontos

print("Valor do salário bruto: ", salario_bruto)
print("Valor pago ao INSS: ", valor_inss)
print("Valor pago ao Sindicato: ", valor_sindicato)
print("Valor pago ao Imposto de Renda: ", valor_ir)
print("O valor do seu salarido liquido vai ser de: ", salario_liquido)
