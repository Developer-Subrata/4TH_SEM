rng=int(input("Enter Range Of Your Fibonacci Series : "))
def fibb(rng):
    if rng<=1:
       return rng
    else:
        return fibb(rng-1)+fibb(rng-2)
for i in range(rng):
    print("\nYour Series Is : ",fibb(i))
