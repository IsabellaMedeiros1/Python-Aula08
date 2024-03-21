print("Média final de alunos")

while True:
    print("Informe seu nome: ")
    nome = input()
    print("Informe sua primeira nota:")
    n1 = float(input())
    print("Informe sua segunda nota: ")
    n2 = float(input())
    print("Informe sua terceira nota: ")
    n3 = float(input())

    media = (n1 + n2 + n3)/3.0
    print("Nome:          1°      2°      3°        Média Final")
    print(f"{nome:<14}{n1:<8.1f}{n2:<8.1f}{n3:<8.1f}{media:>9.1f}")
    print("Deseja calcular a média de outro estudante? [S/N]?")
    escolha = input()
    if escolha == "N":
        break
print("Programa Finalizado")


