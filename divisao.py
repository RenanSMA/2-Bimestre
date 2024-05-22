# DIVISÃO


divisao: float = 0
continuaDividindo = True

while continuaDividindo:
    print("Valor atual:", divisao)
    numero: float = float(input('Digite um número (0 para Encerrar): '))
    if numero != 0:
        if divisao == 0:
            divisao = numero
        else:
            divisao = divisao / numero
    else:
        continuaDividindo = False