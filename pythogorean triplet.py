limit=int(input("Limit="))
(c,m)=(0,2)
while c<limit:
    for n in range(1,m):
        (a,b,c)=(m*m-n*n, 2*m*n, m*m+n**n)
        if c>limit:
            break
        print(a,b,c)
    m=m+1
