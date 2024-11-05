import numpy as np
import math

def sineseries(x,n):
    for i in range (0,n+1,2):
        eventerm=sum(pow(x,i)/math.factorial(i))
    for i in range(1,n+1,2):
        oddterm=sum(pow(x,i)/math.factorial(i))
    sine =  eventerm - oddterm
    return sine

x=int(input("Enter x:"))
print(sineseries(x,10))
print(sineseries(x,100))
