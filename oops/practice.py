class Friends:
    def __init__(self, name, age, hairColor):
        self.name = name
        self.age = age
        self.hairColor = hairColor

    def show(self):
        print("Friends are: ")
        print("name: ", self.name)
        print("age: ", self.age)
        print("hair color: ", self.hairColor)

f1 = Friends("john", 16, "blue")
f1.show()