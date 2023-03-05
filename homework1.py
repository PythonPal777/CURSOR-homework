class Animals:
    def __init__(self, animal_name, animal_age):
        self.name = animal_name
        self.age = animal_age

    def sleep(self):
        print(f"{self.name} is sleeping")

    def eat(self):
        print(f"{self.name} is eating")

class Python(Animals):

    def crawl(self):
        print(f"{self.name} is crawling")

    def hiss(self):
        print(f"{self.name} is hissing")
