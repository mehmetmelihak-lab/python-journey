class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello my name is {self.name} and im {self.age} years old.")

person1 = Person("Alice",19)
print(person1.name)
print(person1.age)
person1.greet()

person2 = Person("Bob",42)
person2.greet()