import numpy as np

# Define a matriz A e o vetor b do sistema linear
A = np.array([[9,5,2], [5,10,3], [2, 3, 6]])
b = np.array([960, 510, 610])

# Define o vetor de solução inicial x0 e o vetor de solução atual x
n = len(A)
x0 = np.zeros(n)
x = np.zeros(n)

# Define o critério de parada
tol = 1e-5

# Define o número máximo de iterações
max_iter = 100

# Implementa o método de Gauss-Seidel
for k in range(max_iter):
    for i in range(n):
        s1 = sum(A[i,j] * x[j] for j in range(i))
        s2 = sum(A[i,j] * x0[j] for j in range(i+1, n))
        x[i] = (b[i] - s1 - s2) / A[i,i]

    # Verifica o critério de parada
    if np.linalg.norm(x - x0) < tol:
        break

    # Atualiza o vetor de solução anterior
    x0 = x.copy()

# Imprime a solução do sistema linear
print("Solução do sistema linear: ", x)
