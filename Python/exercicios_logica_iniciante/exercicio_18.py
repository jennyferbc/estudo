#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

mb = float(input("Informe o tamanho do arquivo em MB: "))
mbps = float(input("Informe a velocidade do link em Mbps: "))

tempo_download = mb / mbps

tempo_download_em_minutos = tempo_download / 60

print("O tempo aproximado de download será: ", tempo_download_em_minutos)

