import numpy as np  # Load numpy
from matplotlib import pyplot as plt  # Load matplotlib

# Parameters
nx = 81          # Number of grid points
nt = 55          # Number of time steps
dx = 2.0 / (nx - 1)  # Spatial step
dt = 0.01       # Time step
c = 1.0          # Wave speed (not used directly in nonlinear case)

# Grid and Initial Condition
x = np.linspace(0, 2, nx)  # Spatial domain
u = np.ones(nx)            # Initial velocity array
u[int(0.5 / dx):int(1 / dx + 1)] = 2  # Set initial condition (top-hat function)

# Time-stepping
for n in range(nt):  # Iterate over time steps
    un = u.copy()    # Save the previous time step
    for i in range(1, nx):  # Update interior points using upwind scheme
        u[i] = un[i] - un[i] * dt / dx * (un[i] - un[i - 1])
    
    u[0] = u[-1]
    # Plot intermediate results every 5 steps
    if n % 5 == 0:
        plt.plot(x, u, label=f"t={n * dt:.2f}")

# Final Plot
plt.xlabel("x")
plt.ylabel("u")
plt.title("Non-linear Advection")
# plt.legend()
# plt.grid()
plt.show()
