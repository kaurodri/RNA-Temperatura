# RNA - Python
import sys
sys.executable

#Célula 1
import numpy as np
import matplotlib.pyplot as plt

#Célula 2
plt.style.use('dark_background')
plt.rcParams['figure.figsize'] = (10, 8)

#CRIAR O DATASET
#Célula 3
def get_linear_curve(x, w, b=0, noise_scale=0):
    return w * x + b + noise_scale*np.random.randn(x.shape[0])

#Célula 4
x = np.arange(-10, 30.1, 0.5)
Y = get_linear_curve(x, 1.8, 32, noise_scale=2.5)

#Célula 5
plt.scatter(x, Y)
plt.xlabel('°C', fontsize=20)
plt.ylabel('°F', fontsize=20)

#Demonstração de Curvatura
# plt.hist(np.random.randn(100000), bins=100, edgecolor='white', linewidth=2);

#MODELO
#Inicializar os pesos e bias
#Feedforward
#Calcular a perda
#Backpropagation

#Célula 6
#Inicializar
w = np.random.rand(1)
b = 0

#Célula 7
def forward(inputs, w, b):
    return w * inputs + b

#Célula 8
def mse(Y, y):
    return (Y - y) ** 2

#Célula 9
def backpropagation(inputs, outputs, targets, w, b, lr):
    dw = lr * (-2 * inputs * (targets - outputs)).mean()
    db = lr * (-2 * (targets - outputs)).mean()

    w -= dw
    b -= db
    return w, b
