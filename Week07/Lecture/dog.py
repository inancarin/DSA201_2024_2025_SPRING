class Dog:
    breed = "Poodle" # class variable
    friends = [] # class variable

    def __init__(self, name):
        self.name = name
        self.closeFriends = [] # instance variable
    
    def addCloseFriend(self, newFriend):
        self.closeFriends.append(newFriend)
    
    def addFriend(self, newFriend):
        self.friends.append(newFriend)
    
    def changeBreed(self, newBreed):
        self.breed = newBreed
    
    def changeName(self, newName):
        self.name = newName
    
    def getName(self):
        return self.name
    
    def getBreed(self):
        return self.breed

    def getCloseFriends(self):
        return self.closeFriends
    
    def getFriends(self):
        return self.friends
