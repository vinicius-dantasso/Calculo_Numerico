
def lagrange(x, xi, yi):
    """
    Calcula o polinômio de Lagrange para uma tabela de pontos (xi, yi) 
    e retorna o valor do polinômio para o ponto x.
    
    Parâmetros:
        x (float): ponto no qual o polinômio deve ser avaliado
        xi (list): lista dos pontos xi da tabela
        yi (list): lista dos pontos yi da tabela
    
    Retorna:
        float: valor do polinômio de Lagrange para o ponto x
    """
    n = len(xi)
    L = 0.0
    
    for i in range(n):
        # Calcula o termo de Lagrange correspondente a xi
        termo = 1.0
        
        for j in range(n):
            if j != i:
                termo *= (x - xi[j]) / (xi[i] - xi[j])
        
        # Acumula o termo no valor do polinômio
        L += yi[i] * termo
    
    return L

xi = [2.4, 3.0, 3.6]
yi = [11.02, 20.08, 36.59]

polinomio = lagrange(3.6, xi, yi)

print(polinomio)
