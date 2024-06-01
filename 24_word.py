words = input("Enter Sequence Of Words : ").split()
dictionary = {}
for word in words:
    fl=word[0].lower()
    if fl in dictionary:
        dictionary[fl].append(word)
    else:
        dictionary[fl]=[word]
print(dictionary)