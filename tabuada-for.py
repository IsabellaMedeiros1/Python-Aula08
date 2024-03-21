print("Digite um numero para mostrar a tabuada")
numero = int(input())
         #inicialização      termino      incremento
for i in range(1              , 11         , 1):
    res = numero * i
    print(f"{numero} x {i:>2} = {res}")
print("Fim da tabuada")