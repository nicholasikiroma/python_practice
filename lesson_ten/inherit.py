class Person(object):

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def Display(self):
        print(self.name, self.id)

class Emp(Person):
    def Print(self):
        print("Emp class called")


Emp_details = Emp("Riley", 1511)

Emp_details.Display()

Emp_details.Print()
