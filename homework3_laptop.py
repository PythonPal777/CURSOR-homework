from abc import ABC, abstractmethod

class Laptop(ABC):
    @abstractmethod
    def screen(self):
        pass

    @abstractmethod
    def keyboard(self):
        pass

    @abstractmethod
    def touchpad(self):
        pass

    @abstractmethod
    def webcam(self):
        pass

    @abstractmethod
    def ports(self):
        pass

    @abstractmethod
    def dynamics(self):
        pass


class LenovoLaptop(Laptop):
    def screen(self):
        print('Lenovo Laptop: 15.6"')

    def keyboard(self):
        print("Lenovo Laptop: mechanical keyboard")

    def touchpad(self):
        print("Lenovo Laptop: Allows you to move cursor")

    def webcam(self):
        print("Lenovo Laptop: webcamera Lenovo")

    def ports(self):
        print("Lenovo Laptop: 3,5 mm audio / USB 3.0 / USB Type C / HDMI / Mini DisplayPort / RJ-45 (LAN 10/100/1000)")

    def dynamics(self):
        print("HP Laptop dynamics")


lenovo_laptop = LenovoLaptop()

lenovo_laptop.screen()
lenovo_laptop.keyboard()
lenovo_laptop.touchpad()
lenovo_laptop.webcam()
lenovo_laptop.ports()
lenovo_laptop.dynamics()
