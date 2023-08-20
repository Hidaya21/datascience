from person import person
from student  import student
def main():
    Hidaya = person("Hidaya",22)
    person2=person("Hamza",17)
    print(Hidaya.say_hi())
    
    std1=student("latifa",18,2021)
    std2=student("Harith",21,2022)
    t1=te
    print(std1.say_hi())
    print(std2.say_hi())
    print(student.say_hi(std2))
    print(Hidaya.get_name())
    Hidaya.set_name("Hidaya Nasser")
    print(Hidaya.get_name())
    print(Hidaya.descrip())
    Hidaya.run()
main()