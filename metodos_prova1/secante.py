def funcao(x):
    # aqui é definida a função desejada
    return x * x * x - x * x + 2

def secante(x0, x1, erro, iteracoes):
    # loop que realiza o cálculo da raiz da função
    x2 = 0
    for i in range(iteracoes):
        # calculando o próximo valor de x
        x2 = x1 - funcao(x1) * (x1 - x0) / (funcao(x1) - funcao(x0))
        if abs(funcao(x2)) < erro:
            return x2
        # atualizando os valores de x0 e x1
        x0 = x1
        x1 = x2
    return x2

x0 = -1.5 # valor inicial x0
x1 = -0.5 # valor inicial x1
erro = 0.0000000001 # erro desejado
iteracoes = 100

x = secante(x0, x1, erro, iteracoes)

print("Zero da função: ", x)