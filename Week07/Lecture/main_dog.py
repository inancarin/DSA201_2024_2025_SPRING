import dog as d

d1 = d.Dog("Rosie")
d2 = d.Dog("Nala")

print(d1.getName())
print(d2.getName())

print(d1.getBreed())
print(d2.getBreed())

d1.changeBreed("French Poodle")

print(d1.getBreed())
print(d2.getBreed())

d1.addFriend("Joe")
print(d1.getFriends())
print(d2.getFriends())

d1.addCloseFriend("Matt")
d2.addCloseFriend("Jackson")
print(d1.getCloseFriends())
print(d2.getCloseFriends())