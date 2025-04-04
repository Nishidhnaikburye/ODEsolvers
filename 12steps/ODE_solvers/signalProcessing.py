import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack

# Signal generation function
def signal_samples(t):
    """
    Generate a signal composed of two sinusoidal components and random noise.

    Parameters:
    t (array-like): Time values for which the signal is generated.

    Returns:
    array-like: Signal values for the corresponding time points.
    """
    return (2 * np.sin(2 * np.pi * t) +  # First sine wave component
            3 * np.sin(22 * 2 * np.pi * t) +  # Second sine wave component
            2 * np.random.randn(*np.shape(t)))  # Random noise

# Parameters for sampling
B = 30.0  # Bandwidth in Hz
f_s = 2 * B  # Sampling frequency in Hz
delta_f = 0.01  # Frequency resolution in Hz
N = int(f_s / delta_f)  # Number of samples
T = N / f_s  # Sampling period in seconds

# Print calculated parameters
print(f"N (Number of samples) = {N}")
print(f"T (Sampling period) = {T} seconds")

# Create time array and sample the signal
t = np.linspace(0, T, N)
f_t = signal_samples(t)

# Compute Fourier Transform and frequencies
F = fftpack.fft(f_t)  # FFT of the signal
f = fftpack.fftfreq(N, 1.0 / f_s)  # Frequency bins
mask = np.where(f >= 0)  # Only positive frequencies

# Plot the Fourier Transform results
fig, axes = plt.subplots(3, 1, figsize=(8, 6))

# Logarithm of FFT magnitude
axes[0].plot(f[mask], np.log(abs(F[mask])), label="real")
axes[0].plot(B, 0, 'r*', markersize=10)  # Mark bandwidth
axes[0].set_ylabel("$\log(|F|)$", fontsize=14)
axes[0].set_title("Logarithm of FFT Magnitude")

# Normalized FFT magnitude (Full spectrum)
axes[1].plot(f[mask], abs(F[mask]) / N, label="real")
axes[1].set_xlim(0, 2)
axes[1].set_ylabel("$|F|/N$", fontsize=14)
axes[1].set_title("Normalized FFT Magnitude (0-2 Hz)")

# Normalized FFT magnitude (Zoomed in 21-23 Hz)
axes[2].plot(f[mask], abs(F[mask]) / N, label="real")
axes[2].set_xlim(21, 23)
axes[2].set_xlabel("Frequency (Hz)", fontsize=14)
axes[2].set_ylabel("$|F|/N$", fontsize=14)
axes[2].set_title("Normalized FFT Magnitude (21-23 Hz)")

plt.tight_layout()
plt.show()

# Frequency-domain filtering
F_filtered = F * (abs(f) < 2)  # Apply a low-pass filter (frequencies below 2 Hz)
f_t_filtered = fftpack.ifft(F_filtered)  # Inverse FFT to obtain the filtered signal

# Plot the original and filtered signals
fig, ax = plt.subplots(figsize=(8, 3))
ax.plot(t, f_t, label='Original', alpha=0.7)
ax.plot(t, f_t_filtered.real, color="red", lw=2, label='Filtered')  # Real part of the filtered signal
ax.set_xlim(0, 10)
ax.set_xlabel("Time (s)")
ax.set_ylabel("Signal")
ax.legend()
ax.set_title("Original vs Filtered Signal (Low-pass filter < 2 Hz)")

plt.tight_layout()
plt.show()
