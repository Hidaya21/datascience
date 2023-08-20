class prodect:
    #constructor
    def __init__ (self,name,category,price):
        self.name=name
        self.category=category
        self.price=price
    def get_name():
        return self.name
    def get_category():
        return self.category
    def get_price():
        return self.price
    def set_name(self,newName):
        self.name=newName      
    def discrip(self):
        print f"prodect {self.name} is {self.category} cost{self.price}"
    def discount(self,amount):
        self.price= self.price - (self.price * amount/100)
        if self.category ="Electonic":
            self.price += 10
        
        
        
    
        