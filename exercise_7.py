class vehicle():
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def __str__(self):
        return f"базовий клас всіх транспортних засобів. має характеристики: \n" \
               f"рік -  {self.age} \n" \
               f"назва -  {self.name} \n"


class watervehicle(vehicle):
    def __init__(self, age, name):
        super().__init__(age, name)
        self.is_swim = True

    def __str__(self):
        return f"водний клас. має характеристики: \n" \
               f"рік -  {self.age} \n" \
               f"назва -  {self.name} \n" \
               f"може плавати -  {self.is_swim} \n"


class airvehicle(vehicle):
    def __init__(self, age, name):
        super().__init__(age, name)
        self.is_fly = True

    def __str__(self):
        return f"клас літаків. має характеристики: \n" \
               f"рік -  {self.age} \n" \
               f"назва -  {self.name} \n" \
               f"може літати -  {self.is_fly} \n"


class motorizedvehicle(vehicle):
    def __init__(self, age, name):
        super().__init__(age, name)
        self.is_motorized = True

    def __str__(self):
        return f"клас літаків. має характеристики: \n" \
               f"рік -  {self.age} \n" \
               f"назва -  {self.name} \n" \
               f"має мотор -  {self.is_motorized} \n"


class helicopter(airvehicle, motorizedvehicle):
    def __init__(self, age, name):
        super().__init__(age, name)


    def __str__(self):
        return f"клас літаків з мотором (гвинтокрили). має характеристики: \n" \
               f"рік -  {self.age} \n" \
               f"назва -  {self.name} \n" \
               f"має мотор -  {self.is_motorized} \n" \
               f"може літати -  {self.is_fly} \n"


vehicle = vehicle(age=2000, name="базовий клас")
print(vehicle)

water_vehicle = watervehicle(age=1912, name="титанік")
print(water_vehicle)

air_vehicle = airvehicle(age=1916, name="boeing")
print(air_vehicle)

motorized_vehicle = motorizedvehicle(age=1916, name="boeing")
print(motorized_vehicle)

helicopter = helicopter(age=1984, name="apache")
print(helicopter)
