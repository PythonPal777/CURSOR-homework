class Human:
    def eat(self):
        print("Human is eating")

    def sleep(self):
        print("Human is sleeping")

    def study(self):
        print("Human is studying")

    def work(self):
        print("Human is working")


class Animal:
    def ride(self):
        print("Animal is riding")

    def sneak(self):
        print("Animal is sneaking")


class Centaur(Human, Animal):
    def hunt(self):
        print("Centaur is hunting")


centaur = Centaur()

centaur.eat()
centaur.sleep()
centaur.study()
centaur.work()
centaur.ride()
centaur.sneak()

centaur.hunt()



