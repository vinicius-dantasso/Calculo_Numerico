def funcao(x):
    #Função da Questão
    return x**3 - x**2 + 2 #Inserir a função aqui!!

def bissec(a, b, erro, iteracoes):
    # loop que realiza o cálculo da raiz da função
    for i in range(iteracoes):
        # encontrando o ponto médio do intervalo
        x = (a + b) / 2

        if abs(funcao(x)) < erro:
            return x
        # verificando se a raiz está no intervalo [a, x]
        if funcao(a) * funcao(x) < 0:
            # se sim, atualiza o valor de b
            b = x
        else:
            # se não, atualiza o valor de a
            a = x

    return x

# valores dos parâmetros
a = -2 # limite inferior do intervalo
b = -1 # limite superior do intervalo
erro = 0.0000000001 # erro desejado
iteracoes = 100

# chamada da função bisseção
x = bissec(a, b, erro, iteracoes)

# impressão do resultado
print("Zero da função: ", x)