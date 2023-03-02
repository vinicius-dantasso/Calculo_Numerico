import math

def ponto_fixo(f, g, x0, eps, N):
    #f: a função que representa a equação não linear
    #g: a função auxiliar utilizada para encontrar a raiz
    #x0: o valor inicial da iteração
    #eps: a tolerância do erro
    #N: o número máximo de iterações permitido
    #return: a raiz da equação não linear

    i = 0
    x_ant = x0
    
    while i < N:
        x_atual = g(x_ant)
        if abs(x_atual - x_ant) < eps:
            return x_atual
        x_ant = x_atual
        i += 1
    
    return None

def f(x):
    return x**3-9*x+5

def g(x):
    return (x**3+5)/9

x0 = 1.0
eps = 1e-6
N = 100

raiz = ponto_fixo(f, g, x0, eps, N)

if raiz is None:
    print("Não foi possível encontrar a raiz.")
else:
    print("A raiz da equação é: {:.6f}".format(raiz))
