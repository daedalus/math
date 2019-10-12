# Given the following paper: https://www.nature.com/articles/s41598-019-50234-9

#FIXME
# find this function implementation: ToeplitzMultiplyE 

def CZT(x,M,W,A):
    N=len(x)
    X = list(N)
    r = list(N)
    c = list(M)
    for k in range(0,N-1):
        X[k] = W[((k**2)//2)] * A[-k] * x[k]
        r[k] = W[-((k**2)//2)]
    for k in range(0,M-1):
        c[k] = W[-((k**2)//2)]
    X = ToeplitzMultiplyE(r,c,X)
    for k in range(0,M-1):
        X[k] = W[((k**2)//2)] * X[k]
    return X

def ICZT(X,N,W,A):
    M = len(X)
    if M != N:
        raise("M must == to N")
    n = N
    x = list(n)
    for k in range(0,n-1):
        x[k] = W[((k**2)//2)] * X[k]
    p = list(n)
    p[0] = 1
    for k in range(0,n-1):
        p[k] = (p[k-1])*(W[k]-1)
    u = list(n)
    for k in range(0,n-1):
        u[k] = (-1)**k * ((W[(2*(k**2))-((2*n)-1)+n*(n-1)])/(p[n-k-1]*p[k]))
    z = list(n)
    for j = range(n-1,0,-1):
        u1[k] = u[k-j]
    u2 = u[0] + [0] * (n-1)
    x1 = ToeplitzMultiplyE(u1,z,x)
    x1 = ToeplitzMultiplyE(z,u1,x1)
    x2 = ToeplitzMultiplyE(u,u2,x)
    x2 = ToeplitzMultiplyE(u2,u,x2)
    for k in range(0,n-1):
        x[k] = (x2[k] - x1[k])/u[0]
    for k in range(0,n-1):
        x[k] = A[k] * W[-((k**2)//2)] * x[k]
    return x


