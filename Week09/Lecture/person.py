class Person: # Parent class
    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age
    
    def __str__(self):
        return "ID:" + str(self.id )+ ", Name: " + self.name + ", Age: " + str(self.age)
    
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
    def changeAge(self, newAge):
        self.age = newAge

class Doctor(Person):
    def __init__(self, name, id, age, hospital):
        """
        self.name = name
        self.id = id
        self.age = age
        """
        super().__init__(name, id, age)
        self.hospital = hospital

    def __str__(self):
        #return "Dr. " + self.name + " in " + self.hospital
        return "Dr. " + super().getName() + " in " + self.hospital
        
    def getHospital(self):
        return self.hospital

class Student(Person):
    def __init__(self, name, id, age, school):
        super().__init__(name, id, age)
        self.school = school
    
    def __str__(self):
        return super().__str__() + " in " + self.school

# main

d1 = Doctor("Jack", 5, 45, "Acibadem Hospital")
p1 = Person("Alice", 1, 18)
s1 = Student("Rose", 2, 19, "Sabanci University")
print(d1.getName())
print(d1.getHospital())
print(d1)
print(p1)
print(s1)