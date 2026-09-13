""""
How to interpret this script
We first generate a sample signal as the sum of two sine waves with frequencies of 10 Hz and 20 Hz.
We then compute the DFT of the signal using a nested loop that implements the DFT formula.
Next, we compute the FFT of the signal using the np.fft.fft() function from NumPy.
Finally, we plot the original signal and the frequency spectra obtained from both the DFT and FFT.
The output of the script will show the original signal in the top plot, and the frequency spectra
    obtained from the DFT and FFT in the bottom plot.
    The two frequency spectra should be nearly identical,
    demonstrating the equivalence of the two algorithms.

Note that the FFT algorithm is much more efficient than the direct DFT implementation,
    especially for large input sizes. The computational complexity of the DFT is O(N^2),
    while the FFT has a complexity of O(N log N), making it much faster for large values of N.
"""

import numpy as np
import matplotlib.pyplot as plt

# Generate a sample signal
t = np.linspace(0, 1, 1000)
signal = np.sin(2 * np.pi * 10 * t) + np.sin(2 * np.pi * 20 * t)

# Compute the DFT
N = len(signal)
dft = np.zeros(N, dtype=complex)
for k in range(N):
    for n in range(N):
        dft[k] += signal[n] * np.exp(-2j * np.pi * k * n / N)

# Compute the FFT
fft = np.fft.fft(signal)

# Plot the results
fig, ax = plt.subplots(2, 1, figsize=(12, 8))

# Plot the original signal
ax[0].plot(t, signal)
ax[0].set_title("Original Signal")
ax[0].set_xlabel("Time (s)")
ax[0].set_ylabel("Amplitude")

# Plot the DFT and FFT
freqs = np.fft.fftfreq(N, t[1] - t[0])
ax[1].plot(freqs, np.abs(dft), label="DFT")
ax[1].plot(freqs, np.abs(fft), label="FFT")
ax[1].set_title("Frequency Spectrum")
ax[1].set_xlabel("Frequency (Hz)")
ax[1].set_ylabel("Amplitude")
ax[1].legend()

plt.show()