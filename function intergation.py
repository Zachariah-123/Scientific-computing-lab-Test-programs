import scipy.integrate as integrate
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return (1/2*np.pi)*np.exp(-1*x**2/2)

result,error= integrate.quad(f, 0, 10)
print(result)
x = np.linspace(0, 1, 100)
y = [f(xi) for xi in x]

plt.plot(x, y)
plt.plot(result)  # plot the integrated value as a dashed line
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Integrated Function')
plt.show()
