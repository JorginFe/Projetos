import re
import random

REGRESSIVO = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]


def checar_cnpj(doc):
    cnpj = remover_caracteres(doc)
    try:
        if eh_sequencia(cnpj):
            return False
    except:
        return False

    try:
        novo_cnpj = calcular_digitos(cnpj, digito=1)
        novo_cnpj = calcular_digitos(novo_cnpj, digito=2)
    except Exception as error:
        return False

    if novo_cnpj == cnpj:
        return True
    else:
        return False

def eh_sequencia(doc):
    sequencia = doc[0] * len(doc)
    if sequencia == doc:
        return True
    else:
        return False


def remover_caracteres(doc):
    return re.sub(r'[^0-9]', '', doc)


def calcular_digitos(doc, digito):
    if digito == 1:
        i = REGRESSIVO[1:]
        novo_cnpj = doc[:-2]
    elif digito == 2:
        i = REGRESSIVO
        novo_cnpj = doc
    else:
        return None
    soma = 0
    for indice, regressivo in enumerate(i):
        soma += (int(doc[indice]) * regressivo)
    novo_digito = 11 - (soma % 11)
    novo_digito = 0 if novo_digito > 9 else novo_digito
    return f'{novo_cnpj}{novo_digito}'

def gera_cnpj():
    primeiro_digito = random.randint(0, 9)
    segundo_digito = random.randint(0, 9)
    segundo_bloco = random.randint(100, 999)
    terceiro_bloco = random.randint(100, 999)
    quarto_bloco = '0001'

    inicio_cnpj = f'{primeiro_digito}{segundo_digito}{segundo_bloco}' \
                  f'{terceiro_bloco}{quarto_bloco}00'

    novo_cnpj = calcular_digitos(inicio_cnpj, digito=1)
    novo_cnpj = calcular_digitos(novo_cnpj, digito=2)

    return novo_cnpj


def formatar_cnpj(cnpj):
    cnpj = remover_caracteres(cnpj)
    formatado = f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}'
    return formatado

# CNPJ = '04.252.011/0001-10'
#
# if checar_cnpj(CNPJ):
#     print(f'O CNPJ {CNPJ} é valido!')
# else:
#     print(f'O CNPJ {CNPJ} é invalido!')
for i in range(100):
    novo_cnpj = gera_cnpj()
    formatado = formatar_cnpj(novo_cnpj)
    print(formatado)