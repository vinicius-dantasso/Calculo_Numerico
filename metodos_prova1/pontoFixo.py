import math

def funcao(x):
    # Função da Questão
    return x**3-9*x+5

def g(x):
    # ponto g, ou seja, a aproximação da solução
    return (x**3+5)/9

def ponto_fixo(x0, erro, iteracoes):
    x = x0
    # loop que realiza o cálculo da solução
    for i in range(iteracoes):
        # calculando o novo x
        x_novo = g(x)
        # verificando se o erro é suficientemente pequeno
        if abs(x_novo - x) < erro:
            return x_novo
        # atualizando o valor de x
        x = x_novo
    # retorna o último valor de x calculado
    return x

x0 = -1  # ponto inicial
erro = 0.0000000001  # erro desejado
iteracoes = 100  # número máximo de iterações

x = ponto_fixo(x0, erro, iteracoes)

print("Zero da função:", x)
