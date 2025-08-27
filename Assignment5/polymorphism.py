# Class 1
class Alice:
    def move(self):
        print("Alice is singing 🎤")


# Class 2
class Bob:
    def move(self):
        print("Bob is dancing 💃")


# Class 3
class Charlie:
    def move(self):
        print("Charlie is running 🏃")


# Class 4
class Diana:
    def move(self):
        print("Diana is swimming 🏊")


# Demonstration
people = [Alice(), Bob(), Charlie(), Diana()]

for person in people:
    person.move()  # Polymorphism: same method name, different behavior
