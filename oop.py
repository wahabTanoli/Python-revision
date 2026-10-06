class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        self.__brand = value

    def carFullName(self):
        return f"{self.brand} {self.model}"
    
    def fuel_type(self):
        return f"Petrol or Diesel"


# my_car = Car("honda", "civic")
# print(my_car.brand)
# print(my_car.carFullName())
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battey_size = battery_size
    def fuel_type(self):
        return f"Electric Cahrge only"

myElectricCar = ElectricCar("Toyata", "markX", "no-bettery")
# print(myElectricCar.fuel_type())
# print(myElectricCar.model)
# myElectricCar.brand="honda"
print(myElectricCar.brand)
# print(myElectricCar.get_brand())

my_manual_car=Car("toyota","Corolla")
# print(my_manual_car.fuel_type())
