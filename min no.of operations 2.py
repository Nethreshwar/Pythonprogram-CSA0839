def x(s1,s2,a,b):
    if a==0:
        return b
    if b==0:
        return a
    if s1[a-1]==s2[b-1]:
        return x(s1,s2,a-1,b-1)
    return 1+min(x(s1,s2,a,b-1),x(s1,s2,a-1,b),x(s1,s2,a-1,b-1))
s1=input("Enter the s1:")
s2=input("Enter the s2:")
print(x(s1,s2,len(s1),len(s2)))
