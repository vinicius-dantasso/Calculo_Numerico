#Erros
soma = 0
n = 6
for i in range(1,n):
    soma += 1/(i*(i+1)) #Função da questão
print(soma)

erro_exato = 1
erro_abs = erro_exato - soma
print(erro_abs)

erro_relativo = erro_abs/erro_exato
print(erro_relativo)

erro_percentual = erro_relativo*100
print(erro_percentual)