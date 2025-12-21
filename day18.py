class Dog():
    def __init__(self,name,breed,age):
        self.name = name
        self.breed = breed
        self.age = age
    def bark(self):
        print("Whoof whoof")
    def info(self):
        print(f"{self.name} is {self.age} years old and its breed is {self.breed}")

dog1 = Dog("Bruce","Scottish Shorthair",5)
dog1.bark()
print(dog1.name)
print(dog1.breed)
dog1.info()


dog2 = Dog("Freya","Golden",1)
dog2.bark()
dog2.info()
print(dog2.name)
print(dog2.breed)

            
        
    

