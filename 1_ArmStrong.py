r=int(input("Enter Range : "))
print("Armstrong Numbers Are : ",end='  ')
while r>=0:
    t=r
    num=0
    while t>0:
        re=t%10
        num=num+(re**3)
        t=t//10
    if num==r:
        print(num,end="  ")
    r-=1