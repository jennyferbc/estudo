#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) 
# deve pagar uma multa de R$ 4,00 por quilo excedente. 
# João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
# Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 
# Imprima os dados do programa com as mensagens adequadas.


peso_do_peixe = float(input("Digite o peso do peixe: "))
peso_maximo = 50
excesso = peso_do_peixe - peso_maximo 
multa = excesso * 4


excedeu = peso_do_peixe > 50

if excedeu:
    print("Você excedeu", excesso, "kg do peso maximo, sua multa é:",multa,"reais")
else:
    print("Voce nao excedeu")



