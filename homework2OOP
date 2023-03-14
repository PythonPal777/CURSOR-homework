"""
There is a Person whose characteristics are:
1. Name
2. Age
3. Availability of money
4. Having your own home

Human can:
1. Provide information about yourself
2. Make money
3. Buy a house
There is also a House, the properties of which include:
1. Area
2. Cost

For Home you can:
1. Apply a purchase discount
e.g.: There is also a Small Typical House with a required area of
40m2.

*Realtor:
1. Name
2. Houses
3. Discount that he/she can give you.
*There is only one realtor who handles small houses you wanna
buy. (Singleton)
Realtor is only one in your city and can:
1. Provide information about all the Houses
2. Give a discount
3. Steal your money with 10% chance
"""

import random

class Person:
    def __init__(self, name, age, money, has_home):
        self.name = name
        self.age = age
        self.money = money
        self.has_home = has_home

    def describe(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Money: {self.money}")
        print(f"Has home: {'Yes' if self.has_home else 'No'}")

    def make_money(self, amount):
        self.money += amount

    def buy_home(self, home):
        if self.money >= home.cost:
            self.money -= home.cost
            self.has_home = True
            print(f"{self.name} has buy a house with area {home.area}m2 and pay {home.cost}$")
        else:
            print(f"{self.name} has no money to buy a house.")


class House:
    def __init__(self, area, cost):
        self.area = area
        self.cost = cost

    def apply_discount(self, discount):
        self.cost *= (1 - discount)


class Realtor:
    _instance = None

    def __new__(cls, name, houses, discount):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.name = name
            cls._instance.houses = houses
            cls._instance.discount = discount
        return cls._instance

    def describe_houses(self):
        print("Available houses:")
        for i, house in enumerate(self.houses):
            print(f"{i + 1}. Area: {house.area} m2, Cost: {house.cost}$")

    def give_discount(self, house):
        house.apply_discount(self.discount)
        print(f"{self.name} has  {self.discount * 100}% discount on house with {house.area} m2 area!")

    def steal_money(self, person):
        chance = random.random()
        if chance <= 0.1:
            money_steal = person.money * 0.5
            person.money -= money_steal
            print(f"{self.name} steal {money_steal}$ from {person.name}!")


person = Person("Andriy", 32, 150000, False)
person.describe()
house1 = House(40, 100000)
house2 = House(100, 200000)
realtor = Realtor("Max", [house1, house2], 0.1)
realtor.describe_houses()
realtor.give_discount(house1)
person.buy_home(house1)
person.describe()
realtor.steal_money(person)
