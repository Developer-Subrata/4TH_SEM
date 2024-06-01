s=input("Enter String : ")
half=len(s)//2
f_half=s[:half]
l_half=s[half:]

if f_half==l_half:
    print(f"{s} Is The Symmetrical String !!!")
else:
    print(f"{s} Is Not Symmetrical String !!!")
if s==s[::-1]:
    print(f"BUT, {s} Is The Palindrome String !!!")
else:
    print(f"BUT, {s} Is Not Palindrome String !!!")