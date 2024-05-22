# Verificador de números primos

numero = int(input("Qual número você deseja verificar se é primo? "))

resto = 0

for i in range(1, numero +1):
    if numero % i == 0:
        resto = resto + 1

if resto == 2:
    print("Este número é primo!")
else:
    print("Este número não é primo!")