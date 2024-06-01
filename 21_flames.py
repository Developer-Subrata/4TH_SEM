
print("\t*** Now You Are Playing (F-L-A-M-E-S) Game ***\n")
name11 = input("Enter Name _1:").upper()
name22 = input("Enter Name _2:").upper()

name1 = list(name11)
name2 = list(name22)
dup_lst=[]

for char in name1:
    if char in name2:
        name2.remove(char)
    else:
        dup_lst.append(char)
for char in name2:
    if char in name1:
        name1.remove(char)
    else:
        dup_lst.append(char)

d_ln=len(dup_lst)
print("Remaining UnMatched Characters : ",dup_lst,"\nIts Length Is: ",d_ln)

if d_ln>0:
    flames = {'F': "FRIENDSHIP", 'L': "LOVE", 'A': "AFFECTION", 'M': "MARRIAGE", 'E': "ENEMY", 'S': "SIBLINGS"}
    lst = ['F', 'L', 'A', 'M', 'E', 'S']
    while len(lst) > 1:
        remove_index = (d_ln % len(lst) - 1)
        if remove_index >= 0:
            right = lst[remove_index + 1:]
            left = lst[: remove_index]
            lst = right + left
        else:
            lst = lst[: len(lst) - 1]
    relationship = flames[lst[0]]
    print(f"Relationship For *{name11}* & *{name22}* Is :", relationship)
else:
    print("There Is No Unique Character !!!")
