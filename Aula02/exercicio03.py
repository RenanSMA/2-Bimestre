# O Usuário digitará dois números e será informado as tabuadas presentes entre o primeiro e o segundo número.

num1: int
num2: int = 0



num1 = int(input("Digite o primeiro número para encontrar sua tabuada: "))
num2 = int(input("Digite até qual número você deseja encontrar as tabuadas presentes: "))

print("Aqui está as tabuadas presentes entre os números informados.")

for i in range(num1,num2+1):
  

  for n in range(0,11):
    tabuada = i * n
    print(i, "x", n, "=", tabuada)
