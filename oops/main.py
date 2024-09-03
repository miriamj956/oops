#OOPS - object oriented programming structure
#Class - blueprint of an object, which had properties(atributes) and functions of an object

class Student:
    #properties / attributes 
    #inbuilt function
    def __init__(self, name, age, grade, favColor, hobby):
        self.name = name
        self.age = age
        self.grade = grade
        self.favColor = favColor
        self.hobby = hobby
        self.intro = " "
    #functions / methods
    #user defined
    def showDetails(self):
        print("The details of the students are: ")
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("grade: ", self.grade)
        print("Favorite Color: ", self.favColor)
        print("Hobby: ", self.hobby)

    def introduction(self):
        self.intro = input("Please introduce yourself: ")
        print(self.intro)

#object - instance of a class
#init function gets called automatically when an object is created
s1=Student("Miriam", 15, "10th", "red", "editing")
s1.showDetails()
s1.introduction()

s2=Student("john", 22, "none", "black", "soccer")
s2.showDetails()
s2.introduction()

s3=Student("bob", 17, "12th", "purple", "reading")
s3.showDetails()
s3.introduction()
