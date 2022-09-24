r=int(input())
b=[]
for i in range(1, r + 1):
    if (i**(.5) == int(i**(.5))):
        b.append(i)
print(len(b))
