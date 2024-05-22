# O Usuário vai digitar um número, e será mostrado a tabuada deste número



num: float 



num = float(input("Digite um número para descobrir sua tabuada: "))

print("Aqui está a tabuada do número informado.")
for i in range(0,11):
  tabuada = num * i
  print(num, "x", i, "=", tabuada) # <--- Tabuada do número informado.