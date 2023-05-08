import numpy as np
import matplotlib.pyplot as plt

# Definition der Funktion f(x, y)
def f(x, y):
    return np.exp(-x**2) * np.sin(y)

# Erstellen von Arrays mit den x- und y-Koordinaten
x_coords = np.linspace(-2, 2, 100)
y_coords = np.linspace(-np.pi, np.pi, 100)

# Erstellen des zweidimensionalen Gitters X und Y
X, Y = np.meshgrid(x_coords, y_coords)

# Auswerten der Funktion f an jedem Punkt des Gitters
Z = f(X, Y)

# Erstellen des 2D-Plots
plt.imshow(Z, cmap='viridis', extent=[-2, 2, -np.pi, np.pi])
plt.colorbar()
plt.title('2D-Plot von f(x, y)')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
