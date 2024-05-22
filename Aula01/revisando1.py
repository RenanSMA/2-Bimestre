# Faça um programa em que o usuario insira a quantia de notas para calcular a média destas notas.


quantiaNotas: int
nota: float
soma: float = 0
media: float

print("Calculador de Média de Notas")
print(" ")

quantiaNotas = int(input("Digite a quantia de notas: "))

for i in range(0,quantiaNotas):
  nota = float(input("Digite uma das notas: "))
  soma = soma + nota

media = soma / quantiaNotas

print("A Média destas notas é", media)