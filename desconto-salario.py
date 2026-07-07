def recebe_salario(salario):
    if salario < 2000:
        desconto = 100
    elif salario < 3000:
        desconto = 200
    elif salario < 4000:
        desconto = 300
    else:
        desconto = 0

    return salario - desconto

continuar = "S"

while continuar == "S":
    salario = float(input("Digite o salário: R$ "))
    resultado = recebe_salario(salario)
    print(f"Salário final: R$ {resultado:.2f}")

    continuar = input("Deseja calcular outro salário? (S/N): ").upper()

print("Programa encerrado!")
