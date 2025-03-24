import person as p
#from person import Person 

#p1 = Person()
p1 = p.Person() # p1 is an instance of Person class
p2 = p.Person() # p2 is another instance of Person class

print("Person1:", p1.name, p1.age, p1.address)
print("Person2:", p2.name, p2.age, p2.address)

p3 = p.newPerson(name="John", age=30)
p4 = p.newPerson(name="Rose", age=28)
print("Person3:", p3.name, p3.age, p3.address)
print("Person3:", p3)

myList = []
myList.append(p3)
myList.append(p4)
print(myList)

print(p4.getName())
p4.changeName("Alice")
print(p4.getName())
print(p4.getAge())
p4.changeAge(20)
#p4.age = 30
print(p4.getAge())

