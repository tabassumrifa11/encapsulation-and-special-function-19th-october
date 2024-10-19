class Point:
    
    def __init__(self, x, y, word):
        self.x = x
        self.y = y
        self.word = word
        
        
    def __str__(self):
        return f"({self.x}, {self.y} )"
    
    
    def __len__(self):
        return int(self.word)
    
    
p1 = Point(2, 3, "550")
print(p1)


a = len(p1)
print(len(p1))
print(type(a))