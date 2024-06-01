str=["eat","tea","tan","ate","nat","bat"]
dic={}
for i in str:
    ana="".join(sorted(i))
    if ana in dic:
        dic[ana].append(i)
    else:
        dic[ana]=[i]
print(list(dic.values()))