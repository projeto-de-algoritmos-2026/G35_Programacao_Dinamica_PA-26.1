def calcular_importancia(dificuldade, dias_prova):

    dias_reais = max(1, dias_prova)
    importancia = (dificuldade * 100) / dias_reais
    
    return round(importancia, 2)

def otimizar_estudos(disciplinas, horas_disponiveis):

    W = int(horas_disponiveis * 2) 
    n = len(disciplinas)
    
    valores = []
    pesos_blocos = []
    
    for d in disciplinas:
        valores.append(calcular_importancia(d['dificuldade'], d['dias_prova']))
        pesos_blocos.append(int(d['horas_necessarias'] * 2))

    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            peso_atual = pesos_blocos[i - 1]
            valor_atual = valores[i - 1]
            
            if peso_atual <= w:
                dp[i][w] = max(valor_atual + dp[i - 1][w - peso_atual], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]
                
    itens_selecionados = []
    w_atual = W
    
    for i in range(n, 0, -1):
        if dp[i][w_atual] != dp[i - 1][w_atual]:
            itens_selecionados.append(disciplinas[i - 1])
            w_atual -= pesos_blocos[i - 1]
            
    itens_selecionados.reverse()
    valor_total = dp[n][W]
    
    return itens_selecionados, valor_total