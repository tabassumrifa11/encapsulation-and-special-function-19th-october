class computer:
    def __init__(self):
        self.__maxprice = 900
        
        
    def printPrice(self):
        print(f"Selling price: {self.__maxprice}")
        
        
    def setMaxPrice(self, price):
        self.__maxprice = price
        
        
c = computer()

c.printPrice()

c.__maxprice = 1000
c.printPrice()

c.setMaxPrice(1500)
c.printPrice()