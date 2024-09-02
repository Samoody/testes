def soma_variavel():
    INDICE = 13
    SOMA = 0
    K = 0

    while K < INDICE:
        K += 1
        SOMA += K

    print("1) Valor da variável SOMA:", SOMA)



def is_fibonacci_number(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n or n == 0

def verificar_fibonacci():
    number = int(input("2) Digite um número para verificar na sequência de Fibonacci: "))

    if is_fibonacci_number(number):
        print(f"O número {number} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {number} não pertence à sequência de Fibonacci.")



def analisar_faturamento():
    import json

    
    faturamento_json = '''
    {
        "faturamento": [1200, 800, 0, 2500, 1500, 0, 2100, 1400, 0, 3000, 2300, 0, 1600]
    }
    '''

    dados = json.loads(faturamento_json)
    faturamento = [dia for dia in dados["faturamento"] if dia > 0]

    menor_faturamento = min(faturamento)
    maior_faturamento = max(faturamento)
    media_mensal = sum(faturamento) / len(faturamento)
    dias_acima_da_media = len([dia for dia in faturamento if dia > media_mensal])

    print("3) Análise do faturamento diário:")
    print(f"Menor faturamento: R${menor_faturamento:.2f}")
    print(f"Maior faturamento: R${maior_faturamento:.2f}")
    print(f"Dias com faturamento acima da média: {dias_acima_da_media}")


def calcular_percentual_faturamento():
    faturamento_estados = {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "Outros": 19849.53
    }

    faturamento_total = sum(faturamento_estados.values())

    print("4) Percentual de faturamento por estado:")
    for estado, valor in faturamento_estados.items():
        percentual = (valor / faturamento_total) * 100
        print(f"{estado}: {percentual:.2f}%")



def inverter_string(s):
    string_invertida = ""
    for i in range(len(s) - 1, -1, -1):
        string_invertida += s[i]
    return string_invertida

def inverter_string_usuario():
    string = input("5) Informe  uma string para inverter: ")
    print("String invertida:", inverter_string(string))



soma_variavel()
verificar_fibonacci()
analisar_faturamento()
calcular_percentual_faturamento()
inverter_string_usuario()


