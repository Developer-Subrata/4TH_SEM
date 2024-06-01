lst=['P','Y','T','H','O','N']
temp1=lst[0]
temp2=lst[len(lst)-1]
lst[0]=temp2
lst[len(lst)-1]=temp1
print(lst)