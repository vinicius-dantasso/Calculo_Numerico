def funcao(x):
    # Função da Questão
    return x**3 + x**2 + x - 2

def falsaPosicao(a, b, erro, iteracoes):
# loop que realiza o cálculo da raiz da função
    x = 0
    for i in range(iteracoes):
        x = b - (funcao(b) * (a - b)) / (funcao(a) - funcao(b))

        if abs(funcao(x)) < erro:
            return x

        if funcao(a) * funcao(x) < 0:
            b = x
        else:
            a = x

    return x

a = 0 # limite inferior do intervalo
b = 1 # limite superior do intervalo
erro = 0.0000000001 # erro desejado
iteracoes = 100

x = falsaPosicao(a, b, erro, iteracoes)

print("Zero da função:", x)