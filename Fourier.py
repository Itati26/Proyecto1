import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Tiempo y parámetros
t = np.linspace(-np.pi, np.pi, 1000)

# Función de suma de Fourier
def fourier_sum(n_terms):
    f = np.zeros_like(t)
    for n in range(1, 2 * n_terms, 2):  # Solo impares
        f += (4 / (np.pi * n)) * np.sin(n * t)
    return f

# Crear figura y ejes
fig, ax = plt.subplots(figsize=(10, 4))
plt.subplots_adjust(bottom=0.25)  # Espacio para el slider

# Gráficas iniciales
fourier_line, = ax.plot(t, fourier_sum(1), 'r-', label='Aproximación Fourier')
ideal_line, = ax.plot(t, np.sign(np.sin(t)), 'b--', label='Onda cuadrada ideal', alpha=0.5)

# Configurar gráfico
ax.set_xlim(-np.pi, np.pi)
ax.set_ylim(-1.5, 1.5)
ax.set_xlabel('t')
ax.set_ylabel('f(t)')
ax.set_title('Aproximación con 1 armónicos')
ax.grid(True)
ax.legend()

# Crear eje del slider
ax_slider = plt.axes([0.2, 0.1, 0.6, 0.03])
slider = Slider(ax_slider, 'Armónicos', valmin=1, valmax=50, valinit=1, valstep=1)

# Función que actualiza la gráfica
def update(val):
    n = int(slider.val)
    y = fourier_sum(n)
    fourier_line.set_ydata(y)
    ax.set_title(f'Aproximación con {n} armónicos')
    fig.canvas.draw_idle()

# Asociar el slider con la función de actualización
slider.on_changed(update)

plt.show()
