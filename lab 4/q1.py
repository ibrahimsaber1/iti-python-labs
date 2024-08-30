# Q1

class Person:
    def __init__(self, name , age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"hello i am {self.name}")

    def say_age(self):
        print(f"my age {self.age}")

newperson = Person("ibrahim" , 24)

# class SuperHero: that inherits from person

class SuperHero(Person):
    def __init__(self, name , age ,secret_identity , nemesis):
        super().__init__( name , age )
        self.secret_identity = secret_identity
        self.nemesis = nemesis

    def say_hello(self):
        print(f"Hello, I am a superhero named {self.name}.")

    def reveal_secret_identity(self):
        print(f"My secret identity is {self.secret_identity}.")

    def old_say_age(self):
        super().say_age()

    def say_age(self):
        print("its dosent matter how old i am i will kill the joker :)")

p2 = SuperHero("hema",25,"BatMan","El Joker")



# ---------------- --------- -----------------
# ---------------- teasting ------------------
# ---------------- --------- -----------------

# newperson.age
# newperson.say_hello()
# p2.reveal_secret_identity()
# p2.age
# p2.nemesis
# p2.say_age()
# p2.old_say_age()