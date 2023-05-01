import matplotlib.pyplot as plt
from math import sin, pi
import numpy as np


def f(x,y):
    return np.exp(-x**2)*np.sin(y)
x = np.linspace(-np.pi, np.pi, 50)
y = np.linspace(-2,2,50)



plt.plot(x,y, "k-")
plt.title("Sinus und Cosinus") #Titel wird gesetzt
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.axis("equal")                      
plt.show()