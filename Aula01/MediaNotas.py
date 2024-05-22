
# EXEMPLO: Média de 5 notas

nota: float
soma: float = 0
mediaFinal: float

quantiaNotas: int

quantiaNotas = int(input("Digite a quantia de notas desejadas para calcular a média:"))

for i in range(0,quantiaNotas):
  nota = float(input("Digite uma das notas: "))
  soma = soma + nota

mediaFinal = soma / quantiaNotas    # <- fora do laço!


print("A Média das notas informadas é:", mediaFinal)


