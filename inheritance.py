class Animal:
    def walk(self):
        print("walk")


class Dog(Animal):
    def bark(self):
        print("Bark")


class Cat(Animal):
    def mew(self):
        print("Mew Mew")

dog1 = Dog()
dog1.walk()
dog1.bark()

cat = Cat()
cat.walk()
cat.mew()



