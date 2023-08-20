from person import person
class student(person):
    #constructer
    def __init__(self,sname,sage,year):
        super().__init__(sname,sage)
        self.acadimic_year=year
    def say_hi(self):
        return f"Hello {self.name} as student"
    