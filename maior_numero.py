def maior_numero (a,b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return 'Os números são iguais'
        
resultado1 = maior_numero(25,10)
resultado2 = maior_numero(30,30)
resultado3 = maior_numero(31,47)

print('Resultado 1:', resultado1)
print('Resultado 2: ', resultado2)
print('Resultado 3: ', resultado3)
