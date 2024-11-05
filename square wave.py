import numpy as np
import matplotlib.pyplot as plt

def square_wave_fourier_series(x, terms):
    y = np.zeros_like(x)
    for n in range(1, terms * 2, 2):
        y += (4 / np.pi) * (np.sin(n * x) / n)
    return y


x = np.linspace(-np.pi, np.pi, 1000)
y5t = square_wave_fourier_series(x, 5)
y20t = square_wave_fourier_series(x, 20)


def fivet():
    plt.subplot(1, 2, 1)
    plt.plot(x, y5t, label="5 Terms", color='blue')
    plt.title("Fourier Series Approximation of Square Wave\nFirst 5 Terms")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid()
    plt.legend()

def twentyt():
    plt.subplot(1, 2, 2)
    plt.plot(x, y20t, label="20 Terms", color='green')
    plt.title("Fourier Series Approximation of Square Wave\nFirst 20 Terms")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid()
    plt.legend()
fivet()
twentyt()
plt.tight_layout()
plt.show()
