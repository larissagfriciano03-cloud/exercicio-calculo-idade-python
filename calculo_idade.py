from datetime import datetime

def calcular_idade(nascimento):
    ano_atual = datetime.now().year
    idade = ano_atual - nascimento
    return idade

nascimento1 = 2003
idade1 = calcular_idade(nascimento1)

print('Idade 1:', idade1)
