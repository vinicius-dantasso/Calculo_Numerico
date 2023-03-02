import numpy as np

def decomporLU(A):
    n = A.shape[0]
    L = np.eye(n)
    U = np.zeros((n,n))
    
    for j in range(n):
        for i in range(j+1):
            soma1 = sum([L[i,k]*U[k,j] for k in range(i)])
            U[i,j] = A[i,j] - soma1
        
        for i in range(j+1,n):
            soma2 = sum([L[i,k]*U[k,j] for k in range(j)])
            L[i,j] = (A[i,j] - soma2)/U[j,j]
    
    LU = [L, U]
    return LU

def resolverSistema(A, b):
    n = A.shape[0]
    x = np.zeros(n)
    
    for i in range(n-1,-1,-1):
        soma = sum([A[i,j]*x[j] for j in range(i+1,n)])
        x[i] = (b[i] - soma) / A[i,i]
    
    return x

# Definindo a matriz dos coeficientes
A = np.array([[1, 2, 3], [2, 5, 2], [6, 2, 4]])

# Aplicando a decomposição LU
LU = decomporLU(A)
L = LU[0]
U = LU[1]

# Exibindo as matrizes L e U
print("Matriz L:")
print(L)

print("Matriz U:")
print(U)

# Resolvendo o sistema Ly = b
b = np.array([6, 5, 7])
y = resolverSistema(L, b)

# Resolvendo o sistema Ux = y
x = resolverSistema(U, y)

# Exibindo a solução
print("Solução:", x)
