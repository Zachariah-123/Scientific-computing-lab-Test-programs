import numpy as np
def inputmat(n):
    a=np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            a[i][j]= int(input(f"Enter the {i}{j} element:"))
    return a


def eigA(a):
    eigenvalues,eigenvectors = np.linalg.eig(a)
    print(f"eigen values = {eigenvalues}")
    print(f"eigen vectors =\n {eigenvectors}")


def main():
    a=int(input("Enter rows:"))
    b=int(input("Enter columns:"))
    if a==b:
        x=inputmat(a)
        print(x)
        eigA(x)
    else:
        print('Error: Not a square Matrix')
main()
input()
