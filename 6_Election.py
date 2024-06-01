from collections import Counter
candidates={'AJOY':0,'BIJOY':0,'SUJOY':0}
print("Our Candidates : ",candidates.keys())
c=10
while c>0:
    vt=input("A>> AJOY\tB>> BIJOY\tS>> SUJOY\n---> ").lower()
    if vt=='a':
        candidates['AJOY']+=1
    if vt=='b':
        candidates['BIJOY']+=1
    if vt=='s':
        candidates['SUJOY']+=1
    c-=1
winner=Counter(candidates)
result=list(winner.keys())
print("Winner Of The Election Is : ",result[0])