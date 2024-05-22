opçao:int = 1


while opçao != 0:
  print('Calculadora')
  print(' ')
  print('1 - Soma')
  print('2 - Subtração')
  print('3 - Multiplicação')
  print('4 - Divisão')
  print('0 - Sair')
  opçao = int(input('Selecione uma Operação: '))

  if opçao >= 1 and opçao <= 4:
  
    #SOMA
    if opçao == 1:
      soma:float = 0
      continuaSomando = True
      while continuaSomando == True:
        print("A soma está valendo:", soma)
        numero:float = float(input('Digite um número (0 para Encerrar): '))
        if numero != 0:
          soma = soma + numero
        else:
          continuaSomando == False

    # SUBTRAÇÃO
    elif opçao == 2:
      sub:float = 0
      continuaSub = True
      while continuaSub == True:
        print("A Subtração está valendo:", sub)
        numero:float = float(input('Digite um número (0 para Encerrar): '))
        if numero != 0:
          sub = sub + numero
        else:
          continuaSub == False

    # MULTIPLICAÇÃO
    elif opçao == 3:
      multiplicador:float = 1
      continuaMulti = True
      while continuaMulti == True:
        print("A Multiplicação está valendo:", multiplicador)
        numero:float = float(input('Digite um número (0 para Encerrar): '))
  
        if numero != 0:
          multiplicador = multiplicador * numero
        else:
          continuaMulti = False
    
    # DIVISÃO
    elif opçao == 4:
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



