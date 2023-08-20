class person:
    #constructor to create objects
    #initialize instance variables
    def __init__(self,name,p_age=20):
        self.name=name
        self.age = p_age
    def say_hi(self):
        return f"Hello {self.name} as student"
    #use term in enscapulation
    #accessor
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def set_name(self,newName):
        self.name=newName
    def set_age(self,newAge):
        self.age =newAge
    def run(self):
        print(self.name, "is runnin")
    def descrip(self):
        return f"Person name {self.name} is {self.age} years old"
