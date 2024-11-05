import matplotlib.pyplot as plt
import numpy as np
def f(n):
    prod=0
    for i in range(1,n+1,2):
        prod+=1/i
    return prod

print(f"Hundred terms value goes to {f(100)}")
print(f"Ten terms value goes to {f(10)}")
