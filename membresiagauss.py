import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Funci�n para calcular la membres�a gaussiana
def gaussiana(x, mu, sigma):
    return np.exp(-((x - mu)**2) / (2 * sigma**2))

# Par�metros de la funci�n de membres�a gaussiana
mu = 0
sigma = 1

# Rango de valores en x
x = np.linspace(-5, 5, 100)

# Rango de valores en y
y = gaussiana(x, mu, sigma)

# Inicializar figura y ejes
fig, ax = plt.subplots()

# Graficar la funci�n de membres�a gaussiana
line, = ax.plot(x, y)

# Funci�n de animaci�n
def update(frame):
    # Cambiar los valores de mu y sigma en cada frame
    global mu, sigma
    mu = np.sin(frame/10)
    sigma = np.abs(np.cos(frame/10))
    y = gaussiana(x, mu, sigma)
    line.set_ydata(y)
    return line,

# Configuraciones de la animaci�n
ani = FuncAnimation(fig, update, frames=np.arange(0, 100, 0.1), interval=50)

# Mostrar la animaci�n
plt.show()
