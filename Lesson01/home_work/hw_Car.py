## Автомобиль
class Car:
    def __init__(self, capacity, gas_per_km, gas=0):
        self.gas_per_km = gas_per_km
        self.capacity = capacity
        self.mileage = 0
        if gas > capacity:
            self.gas = capacity
            print(f"Излишек топлива ")
        else:
            self.gas = gas

    def fill(self, fuel):
        if self.gas + fuel > self.capacity:
            extra_fuel = self.gas + fuel - self.capacity
            self.gas = self.capacity
            print(f"Излишек топлива = {extra_fuel}")
        else:
            self.gas += fuel

    def ride(self, distance):
        max_distance = self.gas / self.gas_per_km
        if distance > max_distance:
            self.mileage += max_distance
            self.gas = 0
            print(f"Вы проехали {max_distance} закончился бензин")
            return max_distance
        else:
            self.gas -= distance * self.gas_per_km
            self.mileage += distance
            return distance

    def get_status(self):
        return f"Топливо: {self.gas}л, Пробег:{self.mileage} км"

car = Car(50, 0.2, 10)
car.ride(60)
car.fill(30)
car.ride(100)
print(car.get_status())

#Vladimir Ghilas
