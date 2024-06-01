def series(term):
    for i in range(term):
        print(" + ",i+1,end=" ")
    sums=(term*(term-1))//2
    return sums
term=int(input("Enter How Many Term You Want : "))
print("Your Series Is : ",end="  ")
print("Sum Of Your Series Is : ",series(term))
