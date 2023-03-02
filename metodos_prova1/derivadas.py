import numpy as np

def f(x):
    return x**2 -2*x +789

p=float(input("Digite o valor do ponto: "))

h=float(input("Digite o valor do acréscimo: "))

derivada1 = (f(p+h)-f(p))/(h)

derivada2 = (f(p+h)-f(p-h))/(2*h)

derivada3 = (f(p-2*h)+8*f(p+h)-8*f(p-h)-f(p+2*h))/(12*h)

print("A derivada1 é", derivada1)

print("A derivada2 é", derivada2)

print("A derivada2 é", derivada3)