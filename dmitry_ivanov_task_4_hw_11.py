class Car:

    def __init__(self, brand='Jeep', model='Renegade', color='black', power=180):
        self.brand = brand
        self.model = model
        self.color = color
        self.power = power

    def specifications(self):  # function, that return dict{attribute name: attribute value}
        specifications = self.__dict__.items()
        return specifications


MyCar = Car()  # create class example

print(MyCar.specifications())

