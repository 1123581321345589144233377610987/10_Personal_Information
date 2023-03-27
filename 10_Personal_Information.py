class PI:
    def __init__(self):
        self.name = ""
        self.address = ""
        self.age = 0
        self.phone = ""
    def set_name(self, name):
        self.name = name
    def set_address(self, address):
        self.address = address
    def set_age(self, age):
        self.age = age
    def set_phone(self, phone):
        self.phone = phone
    def get_name(self):
        return self.name
    def get_address(self):
        return self.address
    def get_age(self):
        return self.age
    def get_phone(self):
        return self.phone

def main():
    my_PI = PI()
    my_PI.set_name("Mike Baye")
    my_PI.set_address("Ogallala, NE")
    my_PI.set_age(43)
    my_PI.set_phone("1-123-581-3213")
    print(f"{my_PI.get_name()}, age {my_PI.get_age()}")
    print(f"{my_PI.get_address()}")
    print(f"{my_PI.get_phone()}")

    my_PI_2 = PI()
    my_PI_2.set_name("Susan Loriman")
    my_PI_2.set_address("Hershey, PA")
    my_PI_2.set_age(26)
    my_PI_2.set_phone("769-342-7281")
    print(f"\n{my_PI_2.get_name()}, age {my_PI_2.get_age()}")
    print(f"{my_PI_2.get_address()}")
    print(f"{my_PI_2.get_phone()}")

    my_PI3 = PI()
    my_PI3.set_name("Toni Terintino")
    my_PI3.set_address("Territown, NY")
    my_PI3.set_age(48)
    my_PI3.set_phone("555-555-5532")
    print(f"\n{my_PI3.get_name()}, age {my_PI3.get_age()}")
    print(f"{my_PI3.get_address()}")
    print(f"{my_PI3.get_phone()}")

    my_PI4 = PI()
    my_PI4.set_name("Jimmy Jahonga")
    my_PI4.set_address("Lajolla, CA")
    my_PI4.set_age(23)
    my_PI4.set_phone("379-274-4747")
    print(f"\n{my_PI4.get_name()}, age {my_PI4.get_age()}")
    print(f"{my_PI4.get_address()}")
    print(f"{my_PI4.get_phone()}")
main()