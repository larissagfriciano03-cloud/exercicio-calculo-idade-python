def verificar_par(valor):
    if valor % 2 == 0:
        return 'PAR'
    else:
        return 'IMPAR'

valor1 = 200
valor2 = 550

numero1 = verificar_par(valor1)
numero2 = verificar_par(valor2)

print('Numero 1:', numero1)
print('Numero 2:', numero2)
