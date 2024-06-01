print("*****STUDENT MANAGEMENT SYSTEM*****\n")
db=[]
def add():
    s=int(input("How Many Student : "))
    for i in range(s):
        temp=[]
        print(f"***{i+1} Student'S Data***")
        temp.append(input("Enter Roll_No : "))
        temp.append(input("Enter Name : "))
        temp.append(input("Enter Stream : "))
        temp.append(input("Enter Current Year : "))
        db.append(temp)

def display():
     print("Roll_No\t Name\t Stream\t Year\n")
     for i in range(len(db)):
        for j in range(len(db[i])):
            print((db[i])[j],end=" \t")
        print()
def delete():
     r=int(input("Enter Roll No To Delete : "))
     del db[r-1]
     
while True:
    ch=int(input("1> Add\t2> Display\t 3> Delete\t 4> EXIT\n---> "))
    if ch==1:
        add()
    elif ch==2:
        display()
    elif ch==3:
        delete()
    elif ch==4:
        exit()
    else:
        print("Enter Correct Choice !!!")


