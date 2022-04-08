#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. 
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math
area_a_ser_pintada = int(input("Informe quantos metros quadrados seram pitados: "))

valor_lata = 80.00
valor_galao = 25.00
litros_necessarios = area_a_ser_pintada / 6
latas_necessarias = math.ceil(litros_necessarios / 18)
galoes_necessarios = math.ceil(litros_necessarios / 3.6)

latas_necessarias2 = latas_necessarias 
galoes_necessarios2 = 0
if litros_necessarios % 18 != 0:
    latas_necessarias2 = latas_necessarias - 1
    galoes_necessarios2 = math.ceil((litros_necessarios - (latas_necessarias2 * 18)) / 3.6)


print("Quantidade de latas necessarias: ", latas_necessarias)
print("Valor total de latas: ", latas_necessarias * valor_lata)
print("Quantidade de galões necessarios: ", galoes_necessarios)
print("Valor total de galões: ", galoes_necessarios * valor_galao)
print("Latas necessarias: ", latas_necessarias2, "Galoes necessarios: ", galoes_necessarios2)








