# MULTIPLICAÇÃO

multiplicador:float = 1
continuaMulti = True

while continuaMulti == True:
  print("A Multiplicação está valendo:", multiplicador)
  numero:float = float(input('Digite um número (0 para Encerrar): '))
  
  if numero != 0:
    multiplicador = multiplicador * numero
  else:
    continuaMulti = False

print('Total:', soma)












