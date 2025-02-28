class Animal:
    def make_sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def make_sound(self):
        print("Dog barks")
class Lion(Animal):
    def make_sound(self):
        print("Lion roars")

# Create instances/object/ of Animal and Dog
animal = Animal()
dog = Dog()
lion = Lion() # it is the object of the lion class
lion_2 = Lion()

# Call make_sound on each instance
animal.make_sound()  # Output: Animal makes a sound
dog.make_sound()     # Output: Dog barks
# third instance
lion.make_sound()
lion_2.make_sound()
