## Автомобиль

Описать класс Car
``` python
class Car:
    def __init__(self, capacity: float, gas_per_km: float, gas: float = 0):
        self.gas = gas
        self.capacity = capacity
        self.gas_per_km = gas_per_km
        self.mileage = 0

    def __str__(self):
        return f"Осталось {self.gas} литров, пробег {self.mileage} км."

    def fill(self, liters: float) -> None:
        if self.gas + liters > self.capacity:
            overflow = self.gas + liters - self.capacity
            self.gas = self.capacity
            print(f"Кол-во лишних литров: {overflow}")
        else:
            self.gas += liters

    def ride(self, km):
        gas_per_ride = self.gas_per_km * km
        if self.gas >= gas_per_ride:
            self.gas -= gas_per_ride
            self.mileage += km
        else:
            max_ride_km = self.gas / self.gas_per_km
            self.gas = 0
            self.mileage += max_ride_km

if __name__ == '__main__':
    car = Car(45, 0.08)
    car.fill(50)
    car.ride(100)
    print(car)
    car.ride(1000)
    print(car)
```
**Важно**: названия методов и атрибутов(свойств) в вашем коде, должны соответствовать указанным в задаче.

а) У машины должны быть атрибуты
* "сколько бензина в баке" (gas)
* "вместимость бака" - сколько максимум вмещается бензина (capacity)
* "расход топлива на **один** километр" (gas_per_km)

б) При создании автомобиля, должна быть реализована возможность указывать начальное количество топлива. \
Но по умолчанию автомобиль должен создаваться с пустым баком.

"Вместимость бака" и "расход топлива" должны быть обязательными параметрами конструктора, \
т.е. их необходимо указывать при создании нового автомобиля.

б) Реализуйте метод "залить столько-то литров в бак"

``` python
car.fill(5)  # залили 5 литров
```

Должна учитываться вместительность бака.
Если пытаемся залить больше, чем вмещается, то бак заполняется полностью + print'ом выводится сообщение о лишних литрах

в) метод "проехать сколько-то км"

``` python
car1.ride(50)  # едем 50 км (если хватит топлива) 
```
В результате поездки тратится бензин.
Машина проедет расстояние, на которое хватит топлива.

г) добавить атрибут с пробегом(mileage), который увеличивается в результате вызова .ride()

Новый автомобиль всегда создается с нулевым пробегом.

**Важно**: тщательно протестируйте вашу реализацию!

