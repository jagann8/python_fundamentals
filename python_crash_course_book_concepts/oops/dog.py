# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         print(f"{self.name} is now sitting")
#
#     def roller(self):
#         print(f"{self.name} is roll over")
#
#
# # making the instances of the class
# myDog = Dog('john', 5)
# myDog.sit()
# myDog.roller()

# ========================================
# car

class Car:
    def __init__(self, year, manufacturer, model):
        self.year = year
        self.manufacturer = manufacturer
        self.model = model
        self.odometer = 0

    def get_descriptive_name(self):
        print(f"{self.year} {self.manufacturer} {self.model}")

    def read_odometer(self):
        print(f"This car is {self.odometer} miles on it.")

    def move_odometer(self, limit):
        self.odometer += limit

    def fill_gas_tank(self):
        print('these type of car need fuel tank')


class Battery:
    """A simple model of Electric car """

    def __init__(self, battery_size=100):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"the battery capacity has {self.battery_size} kwh.")

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on full charge")


class ElectricCar(Car):
    def __init__(self, year, manufacturer, model):
        """Initialize attributes from the parent class"""
        super().__init__(year, manufacturer, model)
        self.battery = Battery()

    def get_battery_size(self):
        print(self.battery, ' is a car battery size')

    def fill_gas_tank(self):
        print('these type car dont need gas tank')


myTesla = ElectricCar(2022, 'Tesla', 'model X')
myTesla.get_descriptive_name()
myTesla.get_battery_size()
myTesla.fill_gas_tank()
myTesla.battery.describe_battery()
myTesla.battery.get_range()