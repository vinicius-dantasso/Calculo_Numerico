from numpy import *

import math

import pandas as pd

import numpy as np

print("Método de Newton-Raphson")

valor = int(input("Digite 1 se for usar intervalo ou 2 se for usar um valor inical: "))

if valor==1:

    print("Digite os valores de a e b")

    a=int(input("digite o valor de a:  "))

    b=int(input("digite o valor de b:  "))

    x=a+b/2

elif valor ==2:

    x0 = int(input("Digite seu valor inicial:  "))

    x=x0

else:

    print("Valor digitado incorreto! Reinicie o programa!")

    exit()

precisao = eval(input("Digite o valor do seu erro:  "))

y1= input("Escreva a sua função f")

def f(x):

    y=eval(y1)

    return y

def derivada(x):

    z = (( f(x+precisao)-f(x))/precisao)

    return z

k=1

k1=[]

x1=[]

fxm=[]

k1.append(0)

x1.append(x)

fxm.append(f(x))

while abs(f(x)>precisao):

    x = x - f(x)/derivada(x)

    k1.append(k)

    x1.append(x)

    fxm.append(f(x))

    k=k+1

k2=k

 

df = pd.DataFrame({'iterações':k1, 'x': x1, 'f(x)':fxm})

print(df.to_string(index=False))

 

print("A raiz de f(x)=", y1, "é aproximadamente x=  ", x, "com o número de iterações igual a ", k2)

