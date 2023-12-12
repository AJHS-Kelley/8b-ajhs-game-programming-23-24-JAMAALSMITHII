#Object-Oriented Programing, Jamaal Smith, v0.1

class Person: # Use PascalCase for ClassNames
    def __init__(self,name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    # To String Function -- How the object appears as a string.
    def __str__(self):   
        return f"Name: {self.name}\nThis person is {self.age} years old. \nThey weigh {self.weight} pounds. \n"



person1 = Person("Monkey D. Luffy", 19, 230)
person2 = Person("KANKAN", 23, 210)
print(person1)
print(person2)

if person1.weight > person2.weight:
    print(f"{person1.name}weighs more than {person2.name}.")
elif person1.weight == person2.weight:
    print("Each person weighs the same. \n")
else:
    print(f"{person2.name} weighs more than {person1.name}.")