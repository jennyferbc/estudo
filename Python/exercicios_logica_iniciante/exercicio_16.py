#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00. 
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.



import math
area_a_ser_pintada = int(input("Informe quantos metros quadrados seram pitados: "))

valor_lata = 80.00
litros_usados = area_a_ser_pintada / 3
latas_necessarias = math.ceil(litros_usados / 18)


print("Quantidade de latas necessarias: ", latas_necessarias)
print("Valor total a ser pago: ", latas_necessarias * valor_lata)


