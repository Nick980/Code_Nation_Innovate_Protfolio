#Person class expample

class Person():
    def __init__(self, name, age, height):
        self.name = name
        self.height = height
        self.age = age
        
    def talk(self):
        print(f"Hello, my name is {self.name}, I am {self.age} and I am {self.height}")
    
    def set_hair(self, hair):                       #Setter function
        self.hair = hair
    
    def get_hair(self):                             #Getter function
        print(self.hair)


Will = Person("Will", 31, "6'1\"")
Nick = Person("Nick", 35, "5'11\"")
Bob = Person("Bob", 55, "5'9\"")

# print(Will.name)
# print(Will.age)
# print(Will.height)

# Will.talk()
# Nick.talk()
# Bob.talk()