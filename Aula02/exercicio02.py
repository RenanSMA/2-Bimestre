# O Usuário informará um número e o programa dirá quais números são pares até o número informado.



num: int


num = int(input("Digite um número: "))


for i in range(0,num):
  resultadoPar = i % 2
  if resultadoPar == 0:
    print(i)

