# Verificador de Números Primos!

numero: int = int(input("Qual número você deseja verificar se é primo? "))
contadorDeZeros: int = 0


for i in range(1,numero+1):
  print(numero, "/", i, "resto:", numero % i)
  if numero % i == 0:
    contadorDeZeros = contadorDeZeros +1 # Forma Abreviada: contadorDeZeros += 1

if contadorDeZeros == 2:
  print("O número informado é Primo!")
elif contadorDeZeros > 2:
  print("O número informado não é Primo!")


