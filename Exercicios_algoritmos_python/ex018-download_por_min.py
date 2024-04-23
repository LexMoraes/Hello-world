#18. Faça um programa que peça o tamanho de um arquivo para download (em MB)
#e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado
#de download do arquivo usando este link (em minutos).

def download_por_min():
    print("---------------------------------------------------------------")
    print("-- Bem vindo(a) à ferramenta de calculo de tempo de download --")
    print("---------------------------------------------------------------")
    print("")

download_por_min()

arquivo = float(input('Informe o tamanho do arquivo a ser baixado(em mega-bytes): '))
velocidade = float(input('Insira a velocidade da internet atual (em Mbps): '))

download = (arquivo / velocidade)/60

print(f"Tempo de download estimado: {download} min")