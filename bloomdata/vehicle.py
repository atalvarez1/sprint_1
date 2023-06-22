
'''
This file holds two classes: Vehicle and Convertible.
They are parent and child class.
'''

# Imagine I want to list these vehicles on Craigslist
# "Parent" class is the more generic of the two classes that I'm working with


class Vehicle:
    '''
    This is a vehicle class
    '''

    def __init__(self, make, model, color, year, mileage):
        self.make = make
        self.model = model
        self.color = color
        self.mileage = mileage
        self.year = year

    def honk(self):
        return "HOOOOOOONK!"
    
    def drive(self, miles_driven):
        self.mileage += miles_driven
        return self.mileage
    
    def __repr__(self):
        return f'''A {self.year} {self.color} {self.make} 
                    {self.model} with {self.mileage} miles'''



if __name__ == '__main__':
    my_vehicle = Vehicle('Toyota', 'Camry', 'red', 2012, 25000)

    # print(my_vehicle.make)
    # print(my_vehicle.model)

    # print(my_vehicle.honk())

    # print(my_vehicle)


# The more specific class is called the "Child" class
class Convertible(Vehicle):

    def __init__(self, make, model, color, year, mileage, top_down=True):
        super().__init__(make, model, color, year, mileage)
        self.top_down = top_down

    
    def change_top_status(self):
        if self.top_down:
            self.top_down = False
            return "Top is now up!"
        self.top_down = True
        return "Top is now down!"
    
    def __repr__(self):
        return f"A {self.year} {self.color} {self.make} {self.model} convertible with {self.mileage} miles and the top down {self.top_down}"


if __name__ == '__main__':
    my_vehicle = Convertible('Toyota', 'Camry', 'red', 2012, 25000)

    print(my_vehicle)
    my_vehicle.change_top_status()
    print(my_vehicle)

    print(my_vehicle.honk())
    print(my_vehicle.drive(1000))