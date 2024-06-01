class test:
    def show(self):
        print("WELCOME !!!")
    def show(self,f_name=''):
        print("Welcome ",f_name)
    def show(self,f_name='',l_name=''):
        print("Welcome ",f_name,l_name)
    
obj1=test()
obj1.show()
obj1.show('hello')
obj1.show("hello",'python')
