# DIVISÃO 

divisao:float = 0

continuaDividindo = True
while continuaDividindo == True:
  print('Valor atual:', divisao)
  numero:float = float(input('Digite um número (0 para Encerrar): '))
  numero2:float = float(input('Digite um número (0 para Encerrar): '))
  if numero != 0:
    divisao = numero / numero2
  else:
    continuaDividindo = False