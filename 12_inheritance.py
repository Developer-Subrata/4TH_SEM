print("*****MULTILEVEL*****")
class G_Father:
    def dis(self):
        print("I'm GrandFather !!!")
class Father(G_Father):
    def dis1(self):
        print("I'm Father !!!")
class Son(Father):
    def dis2(self):
        print("I'm Son !!!")
obj=Son()
obj.dis()
obj.dis1()
obj.dis2()

print("*****MULTIPLE*****")
class G_Father:
    def dis(self):
        print("I'm GrandFather !!!")
class Father:
    def dis1(self):
        print("I'm Father !!!")
class Son(G_Father,Father):
    def dis2(self):
        print("I'm Son !!!")
obj=Son()
obj.dis()
obj.dis1()
obj.dis2()

print("*****HIARACHICAL*****")
class G_Father:
    def dis(self):
        print("I'm GrandFather !!!")
class Father(G_Father):
    def dis1(self):
        print("I'm Father !!!")
class Son(G_Father):
    def dis2(self):
        print("I'm Son !!!")
obj1=Son()
obj2=Father()
obj1.dis()
obj2.dis()