import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 10, 500)
I_t = (5/3) * np.exp(-t) * t
plt.figure(figsize=(10, 5))
plt.plot(t, I_t, label='Current I(t)', color='blue')
plt.title('Current Transient through RC Circuit')
plt.xlabel('Time (t)')
plt.ylabel('Current I(t)')
plt.grid()
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(0, color='black', lw=0.5, ls='--')
plt.legend()
plt.xlim(0, 10)
plt.ylim(0, 2)
plt.show()
