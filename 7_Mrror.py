import string
s=input("Enter The String : ")
al=string.ascii_lowercase
ral=al[::-1]

mirr=''
d=dict(zip(al,ral))  #here al is the KEY of DICT and ral is the VALUE
for i in s:
    mirr+=d[i]
print(mirr)
