num1: int
num2: int

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))



for numeroAtual in range(num1,num2 +1):   # <---Tabuadas de cada Número Separadas!
  print("Tabuada do:", numeroAtual)
  
  # TABUADA
  for numeroDaTabuada in range(0,11):      # <---Linhas das Tabuadas!
    tabuada = numeroAtual * numeroDaTabuada
    print(numeroAtual, "x", numeroDaTabuada, "=", tabuada) 