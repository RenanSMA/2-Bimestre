import random

numeroAleatorio: int = random.randint(1,100)
numeroDigitado: int = 0

print('Adivinhe o número sorteado!')
print(' ')

while numeroAleatorio != numeroDigitado:
  numeroDigitado: int = int(input('Digite um número. '))
  print(numeroDigitado)
  
  # CASO MAIOR
  if numeroDigitado > numeroAleatorio:
    print('Dica: o número digitado é maior que o sorteado!')
  
  # CASO MENOR
  elif numeroDigitado < numeroAleatorio:
    print('Dica: o número digitado é menor que o sorteado!')

print('PARABÉNS! VOCÊ ACERTOU! O número sorteado foi', numeroAleatorio)





