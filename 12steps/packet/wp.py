import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from mpl_toolkits.mplot3d import Axes3D

# Parameters
a = 2  # Width of the Gaussian
# k = 2  # Wave number
x = np.linspace(-10, 10, 400)  # Spatial domain
k = 2*x
t_values = np.linspace(0, 2 * np.pi, 100)  # Time steps
omega = k**2 / 2  # Frequency (assuming free-particle dispersion relation)

# Gaussian wave packet function
def gaussian_wave_packet(x, t, a, k, omega):
    return np.exp(-x**2 / (2 * a**2)) * np.exp(1j * (k * x - omega * t))

# Prepare the figure
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-10, 10)
ax.set_ylim(-1.5, 1.5)
ax.set_zlim(-1.5, 1.5)
ax.set_xlabel("x (Space)")
ax.set_ylabel("Re(ψ)")
ax.set_zlabel("Im(ψ)")
ax.view_init(elev=30, azim=120)  # Adjust the view angle

# Plot initialization
line, = ax.plot([], [], [], lw=2)

# Animation update function
def update(t):
    psi = gaussian_wave_packet(x, t, a, k, omega)
    line.set_data(x, psi.real)
    line.set_3d_properties(psi.imag)
    return line,

# Create animation
ani = FuncAnimation(
    fig, update, frames=t_values, interval=50, blit=True
)

# Save as a GIF
ani.save('gaussian_wave_packet_3d.gif', writer=PillowWriter(fps=20))

plt.show()
