class Profile:
    def __init__(self, name, last_name, phone_number, address, email, birthday, age, sex):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age
        self.sex = sex

    def __str__(self):
        return f"[{self.name}, {self.last_name}, {self.phone_number}, {self.address}, {self.email}, {self.birthday}, {self.age}, {self.sex}]"

profile = Profile('Bruce', 'Wayne', '097777777', 'Gotham city', 'www.batman_and_robin.com', '14.12.1990', '32', 'man')

print(profile)