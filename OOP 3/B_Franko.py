class Car():
    def __init__(self, make, model, year, gas, consumption):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
        self.gas_level = gas
        self.fuel_consumption = consumption

    def get_descriptive_name(self):
        """Возвращает аккуратно отформатированное описание."""
        name = str(self.year) + ' ' + self.make + ' ' + self.model
        return name.title()

    def print_gas_level(self):
        print('В баке осталось {0} литров топлива'.format(self.gas_level))

    def print_odometer(self):
        """Выводит пробег машины ."""
        print("This car has " + str(self.odometer) + " km on it.")

    def update_odometer(self, value):
        '''Устанавливает пробег машины по заданному значению'''
        if value > self.odometer:
            self.odometer = value
        else:
            print('вы не можете установить значение меньше текущего')

    def increase_odometer(self, value):
        if value > 0:
            self.odometer += value
        else:
            print('вы не можете скручивать пробег')

    def print_distance_to_refueling(self):
        print('Без заправки вы можете проехать еще {0} километров'.format(self.gas_level/self.fuel_consumption*100))


class ElectricCar(Car):
    def __init__(self, make, model, year, gas, consumption):
        Car.__init__(self, make, model, year, gas, consumption)
        self.battery = Battery(gas)

    def describe_battery(self):
        self.battery.describe_battery()


class Battery():
    """Простая модель аккумулятора электромобиля."""

    def __init__(self, battery_size=70):
        """Инициализирует атрибуты аккумулятора."""
        self.battery_size = battery_size
    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
car0 = Car('audi', 'a4', 2016, 20, 8.3)
car1 = ElectricCar('tesla', 'model s', 2018, 75, 16.4)
print(car0.get_descriptive_name())
print(car1.get_descriptive_name())
car0.update_odometer(280)
car1.update_odometer(1120)
car0.print_gas_level()
car1.describe_battery()
car0.print_distance_to_refueling()
car1.print_distance_to_refueling()