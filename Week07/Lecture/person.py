class Person:
    age = 20
    name = "Jack"
    address = "Orhanli/Tuzla/Istanbul"


class newPerson:
    def __init__(self, name, age=20, add="Orhanli/Tuzla/Istanbul"):
        self.age = age
        self.name = name
        self.address = add
    
    def __str__(self):
        return "Name is " + self.name + ", age is " + str(self.age)
    
    def __repr__(self):
        return "\"" + self.name + "->" + str(self.age) + "\""
    
    # getter
    def getName(self):
        return self.name
    
    # setter
    def changeName(self, newName):
        self.name = newName
    
    def getAge(self):
        return self.age
    
    def increaseAge(self):
        self.age += 1
    
    def changeAge(self, newAge):
        if isinstance(newAge, int):
            if newAge > 0:
                self.age = newAge
            else:
                print("The age must be positive")
        else:
            print("The age must be integer")

        