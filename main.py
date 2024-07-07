class Human:

    def __init__(self,eyes,hand):
        self.eyes=eyes
        self.hand=hand
    def getInfo(self):
        return "I am a human"
    def display(self):
        eye="Human have {} eyes".format(str(self.eyes))
        hands="Human have {} hands".format(str(self.hand))
        return eye +" " +hands
    def eat(self):
        return "Can eat"
    
class Universe:
    def __init__(self,name):
        self.name=name
    def creatures(self):
        return "There are many creatures in our universe of which {} is one ".format(self.name)

class Animal(Human,Universe):
    def __init__(self,eyes,hands):
        super(Animal,self).__init__(eyes, hands)
    def getInfo(self):
        return "I eat grass and animal"
    def display(self):
        eye="Animal have {} eyes".format(str(self.eyes))
        hands="Animal have {} hands".format(str(self.hand))
        return eye +" " +hands

class Birds(Human):
    def __init__(self,eyes,hands):
        super().__init__(eyes, hands)
    def getInfo(self):
        return "I eat grass only"
    def display(self):
        eye="Birds have {} eyes".format(str(self.eyes))
        hands="Birds have {} hands".format(str(self.hand))
        return eye +" " +hands

def landBirds(Birds):
    def __init__(eyes, hands):
        super(landBirds).__init__(eyes, hands)
        


if __name__ == "__main__":
    human=Human(2,2)
    Bird=Birds(2,0)
    Animals=Animal(2,4)
    print(human.getInfo())
    print(human.display())
    print(human.eat())
    print(Bird.getInfo())
    print(Bird.display())
    print(Bird.eat())
    print(Animals.getInfo())
    print(Animals.display())
    print(Animals.eat())