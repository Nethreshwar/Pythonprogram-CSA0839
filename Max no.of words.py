x=[]
count=0
a=int(input("Enter number of string :"))
for i in range(0,a):
      s=input("Sentence =")
      n.append(s)
for j in x:
      s=j.split()
      count = max(count,len(s))
print(count)
