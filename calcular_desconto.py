def calcular_desconto(valor_produto, percentual_desconto):
    desconto = valor_produto * (percentual_desconto / 100)
    valor_final = valor_produto - desconto
    return valor_final
    
resultado1 = calcular_desconto(200, 10)
resultado2 = calcular_desconto(250, 25)
resultado3 = calcular_desconto(500, 40)

print('Valor final:', resultado1)
print('Valor final:', resultado2)
print('Valor final:', resultado3)
