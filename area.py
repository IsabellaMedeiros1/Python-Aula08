print("Início - cálculo da área retângulo")

while True:

    print("informe a altura do retângulo em cm:")
    altura = float(input())
    print("informe a base do retângulo em cm:")
    base = float(input())

    area = base*altura
    print(f"A área é: {area:5.1f} cm²")

    print("Executar novamente? (S/N)")
    novamente = input()
    if novamente == "N":
        break
print("Fim do programa")