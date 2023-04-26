import numpy as np

# Define a matriz A e o vetor b do sistema linear
A = np.array([[9,5,2], [5,10,3], [2, 3, 6]])
b = np.array([960, 510, 610])

# Calcula a decomposição de Cholesky da matriz A
n = len(A)
L = np.zeros((n, n))

for j in range(n):
    for i in range(j, n):
        s = sum(L[i,k] * L[j,k] for k in range(j))
        if (i == j):
            L[i,i] = np.sqrt(A[i,i] - s)
        else:
            L[i,j] = (1.0 / L[j,j] * (A[i,j] - s))

# Resolve o sistema linear LL'x = b
y = np.zeros(n)
x = np.zeros(n)
y[0] = b[0] / L[0,0]
for i in range(1, n):
    s = sum(L[i,j] * y[j] for j in range(i))
    y[i] = (b[i] - s) / L[i,i]
x[-1] = y[-1] / L[-1,-1]
for i in range(n-2, -1, -1):
    s = sum(L[j,i] * x[j] for j in range(i+1, n))
    x[i] = (y[i] - s) / L[i,i]

# Imprime a solução do sistema linear
print("Solução do sistema linear: ", x)
