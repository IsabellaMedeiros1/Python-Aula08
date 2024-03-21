print("Digite um numero para mostrar a tabuada")
numero = int(input())

i = 1 #inicialização

while i <= 10:  #condição
    res = numero * i
    print(f"{numero} x {i:>2} = {res}")
    i = i + 1   #incremento
print("Fim da tabuada")