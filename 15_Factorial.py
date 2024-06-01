n=int(input("Enter A Number  : "))
def fac(n):
    if n<1:
        return 1
    else:
        return n*fac(n-1)
print(f"Factorial Of {n} Is=> ",fac(n))