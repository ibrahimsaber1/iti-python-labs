# q1 :-------------------------------:)

from datetime import date as d

class Person:
    def __init__(self , name , birthYear):
        self.__name = name
        self.__birthYear = birthYear

    def sayHello(self):
        print(f"hello everyone my name is {self.__name}")

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if type(value) == str and value.rstrip():
            self.__name = value
        else:
            raise ValueError("bro name should be a non empty string...........:)")
    @property    
    def age(self):
        return  d.today().year -self.__birthYear

    @property
    def birthYear(self):
        return self.__birthYear

    @birthYear.setter
    def birthYear(self, value):
        current_year = d.today().year
        if type(value) == int and 0 < value <= current_year:
            self.__birthYear = value
        else:
            raise ValueError("Birth year must be a positive integer and less than or equal to the current year.")




# ---------------- --------- -----------------
# ---------------- teasting ------------------
# ---------------- --------- -----------------


# P1 = Person("iBRAHIM", 2000)
# P1.sayHello()
# print("*" * 70)
# print(P1.name)
# print(P1.age)