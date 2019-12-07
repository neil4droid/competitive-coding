'''
Created on 01-Dec-2019

@author: neil4droid
'''

def decorator_function(input_function):
    def wrapper_function():
        input_function()
    
    return wrapper_function

class Person:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        # self.email = "{}.{}@email.com".format(self.name, self.age)        
    
    @property
    def email(self):
        return "{}.{}@email.com".format(self.name, self.age)
     


    
person = Person("Chinmay", 24, 80)
person.tempattr = 500
print(person.__dict__)
print(type(person))
print(type(person) == Person)
print(type(Person))
print(type(Person) == type)

# print(person)
# print(person.name)
# print(person.age)
# print(person.email)
# 
# person.name = "Tanmay"
# print(person)
# print(person.name)
# print(person.age)
# print(person.email)