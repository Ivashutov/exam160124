import numpy as np

n = int(input())
A=[]
for i in range(n):
    A.append(list(map(float, input().split())))

eigs = np.linalg.eigvals(A)
summ_of_eigs = np.sum(eigs)
print(summ_of_eigs)

