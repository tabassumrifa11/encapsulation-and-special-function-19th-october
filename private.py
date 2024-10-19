print("\033c")

class myClass:
    
    __privateVar = 27
    
    def __privMeth(self):
        print("I'm inside class myClass")
        
        
    def hello(self):
        print("Private Variable value" , myClass.__privateVar)
        
        
foo = myClass()

foo.hello()
print(foo.__privateVar)
foo.__privateVar()