def calculadora(numero1,numero2,operacao):
    if operacao == "+":
        return numero1 + numero2
    elif operacao == "-":
        return numero1 - numero2
    elif operacao == "/":
        if numero2 == 0:
            return "Não é possível dividir por Zero"
        return numero1 / numero2
    elif operacao == "*":
        return numero1 * numero2
    else:
        return "Operação inválida"

resultado1 = calculadora(30,20,"-")
resultado2 = calculadora(50,30,"*")
resultado3 = calculadora(70,40,"+")
resultado4 = calculadora(30,10,"/")
resultado5 = calculadora(225,0,"/")

print('Resultado 1: ',resultado1)
print('Resultado 2: ',resultado2)
print('Resultado 3: ',resultado3)
print('Resultado 4: ',resultado4)
print('Resultado 5: ',resultado5)
