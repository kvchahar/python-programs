def fact(n):
    c=1
    for i in range(1,n+1):
        c=c*i
    return c

x = 5
res = fact(x)
print(res)
