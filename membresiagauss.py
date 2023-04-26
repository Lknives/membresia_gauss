import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Función para calcular la membresía gaussiana
def gaussiana(x, mu, sigma):
    return np.exp(-((x - mu)**2) / (2 * sigma**2))

# Parámetros de la función de membresía gaussiana
mu = 0
sigma = 1

# Rango de valores en x
x = np.linspace(-5, 5, 100)

# Rango de valores en y
y = gaussiana(x, mu, sigma)

# Inicializar figura y ejes
fig, ax = plt.subplots()

# Graficar la función de membresía gaussiana
line, = ax.plot(x, y)

# Función de animación
def update(frame):
    # Cambiar los valores de mu y sigma en cada frame
    global mu, sigma
    mu = np.sin(frame/10)
    sigma = np.abs(np.cos(frame/10))
    y = gaussiana(x, mu, sigma)
    line.set_ydata(y)
    return line,

# Configuraciones de la animación
ani = FuncAnimation(fig, update, frames=np.arange(0, 100, 0.1), interval=50)

# Mostrar la animación
plt.show()
