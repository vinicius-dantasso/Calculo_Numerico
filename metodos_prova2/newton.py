def newton(x, xi, yi):
    """
    Calcula o polinômio de Newton para uma tabela de pontos (xi, yi) 
    e retorna o valor do polinômio para o ponto x.
    
    Parâmetros:
        x (float): ponto no qual o polinômio deve ser avaliado
        xi (list): lista dos pontos xi da tabela
        yi (list): lista dos pontos yi da tabela
    
    Retorna:
        float: valor do polinômio de Newton para o ponto x
    """
    n = len(xi)
    
    # Constrói a tabela de diferenças divididas
    tabela = [[yi[i]] for i in range(n)]
    
    for j in range(1, n):
        for i in range(n-j):
            diff = (tabela[i+1][j-1] - tabela[i][j-1]) / (xi[i+j] - xi[i])
            tabela[i].append(diff)
    
    # Calcula o valor do polinômio
    N = tabela[0][0]
    fator = 1.0
    
    for i in range(1, n):
        fator *= (x - xi[i-1])
        N += tabela[0][i] * fator
    
    return N

xi = [2.6, 3.2, 3.6]
yi = [13.46, 24.53, 36.59]

polinomio = newton(3.8, xi, yi)

print(polinomio)
