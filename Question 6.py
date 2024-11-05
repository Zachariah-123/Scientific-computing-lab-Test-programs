import numpy as np

def inputmat(n,m):
    a=np.zeros((n,m))
    for i in range(n):
        for j in range(m):
            a[i][j]= int(input(f"Enter the {i}{j} element:"))
    return np.array(a)
def dotprod(mat1 ,mat2):
    dotprod=0
    for i in range(n):
        for j in range(n):
            dotprod+=mat1[i][j]*mat2[i][j]
    return dotprod

n=int(input("Emter rank:"))


mat1=inputmat(n,n)
mat2=inputmat(n,n)

def det(a):
    return np.det(a)

det1 = np.linalg.det(mat1)
det2 = np.linalg.det(mat2)
print (det1)
proddet=det1 * det2
print(dotprod(mat1,mat2))
print("The cos of angle between the vectors is" , np.cos(proddet/dotprod(mat1,mat2)))
