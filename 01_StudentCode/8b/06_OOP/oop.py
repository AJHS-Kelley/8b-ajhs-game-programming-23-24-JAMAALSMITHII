#Object-Oriented Programing, Jamaal Smith, v0.4

class Person: # Use PascalCase for ClassNames
    def __init__(self,name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        self.weakness = None
        self.nemesis = None

    # To String Function -- How the object appears as a string.
    def __str__(self):   
        return f"Name: {self.name}\nThis person is {self.age} years old. \nThey weigh {self.weight} pounds. \n"

    def classFunction():
        print("This is an example class function. \n")
        print("It only works when called on an object of that class.")

person1 = Person("Monkey D. Luffy", 19, 230)
person2 = Person("KANKAN", 23, 210)
# print(person1)
# print(person2)

# if person1.weight > person2.weight:
    # print(f"{person1.name}weighs more than {person2.name}.")
# elif person1.weight == person2.weight:
    # print("Each person weighs the same. \n")
# else:
    # print(f"{person2.name} weighs more than {person1.name}.")

# person1.classFunction()

# Changing Properties Afer Creation
print(person1.name)
person1.name = "Twinuzis"
print(person1.name)

# Deleting properties -- DANGER WILL ROBINSON, DANGER!
# THIS IS DOES NOT 'RESET' A PROPERTY, IT DELETES IT COMPLETELY. 
print(person1.name)
del person1.name
# print(person1)

# Deleting Objects -- Delete them if you're finished with them.
del person1

# Adding Properties to Objects 
person2.weakness = "Kryptonite"
print(person2)
print(person2.weakness)