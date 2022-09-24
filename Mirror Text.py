try:
    a=int(input("Enter the number:"))
    r=0
    if(a>0):
        while(a>0):
            d=a%10
            r=r*10+d
            a=a//10
    else:
        c=str(a)
        r=c[::-1]
    print("Mirror image:",r)
except ValueError:
    print("Enter the valied input")
