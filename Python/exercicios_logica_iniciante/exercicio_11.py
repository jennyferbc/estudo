#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#a. O produto do dobro do primeiro com metade do segundo .
#b. A soma do triplo do primeiro com o terceiro.
#c. O terceiro elevado ao cubo.

primeiro = int(input("Informe um numero inteiro: "))
segundo = int(input("Informe outro numero inteiro: "))
terceiro = float(input("Informe um numero real: "))

a = primeiro * 2 + (segundo/2)
b = primeiro * 3 + terceiro
c = terceiro ** 3

print(a)
print(b)
print(c)