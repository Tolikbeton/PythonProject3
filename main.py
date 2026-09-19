import random


class Human:
    def __init__(self, name, car=None):
        self.name = name
        self.car = car
        self.house = House()
        self.money = 100
        self.gladness = 50
        self.satiety = 50

    def work(self):
        self.money += 50
        self.satiety -= 10
        print(f"{self.name} сходил на работу и заработал бабла")

    def shopping(self):
        self.money -= random.randint(5, 10)
        self.house.food += random.randint(1, 10)
        if self.car == None:
            print("Пішли на шопінг пішки")
        else:
            if self.car.drive(random.randint(10, 20)):
                print("Поїхали на шопінг на авто")
            else:
                print("Немає бензину, пішли пішки")

    def eat(self):
        if self.house.food <= 0:
            self.shopping()
        else:
            self.satiety += 10
            self.house.food -= 5
            print(f"{self.name} покушав")

    def chill(self):
        self.gladness += 10
        self.satiety -= 5
        print(f"{self.name} отдых")

    def cleaning(self):
        self.house.pollution = 0
        print(f"{self.name} прибрав у домі")

    def info(self):
        print(f"Ім'я: {self.name}")
        print(f"Гроші: {self.money}")
        print(f"Ситість: {self.satiety}")
        print(f"Настрій: {self.gladness}")
        print(self.house)
        print(self.car)

    def is_alive(self):
        if self.gladness <= 0:
            print("Депресія...")
            return False
        if self.satiety <= 0:
            print("здох з голоду...")
            return False
        if self.money < 0:
            print("Банкрот нема дєнєг...")
            return False
        return True

    def live(self, day):
        print(f"--- День {day} ---")
        self.info()

        dice = random.randint(1, 4)
        if self.satiety < 20:
            self.eat()
        elif self.money < 20:
            self.work()
        elif self.house.food < 10:
            self.shopping()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        elif dice == 3:
            self.chill()
        else:
            self.cleaning()


class Car:
    def __init__(self, model):
        self.model = model
        self.fuel = 60
        self.state = 100

    def drive(self, length):
        delta_fuel = length * 0.1
        if self.fuel - delta_fuel > 0:
            print(f"Ми проїхали {length} км, витратили {delta_fuel} л пального")
            self.fuel -= delta_fuel
            self.state -= length * 0.01
            return True
        else:
            print("Подорож неможлива, не вистачає пального")
            return False

    def add_fuel(self):
        self.fuel += 40
        print("я заправив машинку")

    def __str__(self):
        return f"Авто: {self.model}, пальне: {self.fuel}, стан {self.state}"


class House:
    def __init__(self):
        self.food = 20
        self.pollution = 0

    def __str__(self):
        return f"домик: їжа — {self.food}, бруд — {self.pollution}"


car = Car("Leopard 2A4")
human = Human("марік", car)

for day in range(1, 6):
    if not human.is_alive():
        break
    human.live(day)