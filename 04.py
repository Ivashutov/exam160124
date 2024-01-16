n, m = map(int, input().split())
A=[]
for i in range(n):
    A.append(list(map(int, input().split())))

a=A[0][0]
b=0
c=0
for i in range(n):
    for j in range(m):
        if A[i][j] > a:
            a = A[i][j]
            b=i
            c=j
            
print(b, c, end=' ')
        