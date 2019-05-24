############
### EASY ###
############

# 1
# class TownCar:
#     def __init__(self, car_model):
#           self._model = car_model
#           self._speed = '90 км в час'
#           self._color = 'Красная'
#           self._is_police = 'Не полицейская машина'
#
#     def get_model(self):
#         return self._model
#
#     def get_speed(self):
#         return self._speed
#
#     def get_color(self):
#         return self._color
#
#     def get_is_police(self):
#         return self._is_police
#
#     def go(self):
#         print('Машина поехала')
#
#     def stop(self):
#         print('Машина остановилась')
#
#     def turn(self):
#         print('Машина повернула')
#
# class SportCar:
#     def __init__(self, car_model):
#           self._model = car_model
#           self._speed = '320 км в час'
#           self._color = 'Черная'
#           self._is_police = 'Не полицейская машина'
#
#     def get_model(self):
#         return self._model
#
#     def get_speed(self):
#         return self._speed
#
#     def get_color(self):
#         return self._color
#
#     def get_is_police(self):
#         return self._is_police
#
#     def go(self):
#         print('Машина поехала')
#
#     def stop(self):
#         print('Машина остановилась')
#
#     def turn(self):
#         print('Машина повернула')
#
# class PoliceCar:
#     def __init__(self, car_model):
#           self._model = car_model
#           self._speed = '250 км в час'
#           self._color = 'Синяя'
#           self._is_police = 'Полицейская машина'
#
#     def get_model(self):
#         return self._model
#
#     def get_speed(self):
#         return self._speed
#
#     def get_color(self):
#         return self._color
#
#     def get_is_police(self):
#         return self._is_police
#
#     def go(self):
#         print('Машина поехала')
#
#     def stop(self):
#         print('Машина остановилась')
#
#     def turn(self):
#         print('Машина повернула')
#
# my_car = TownCar('Lada')
# print(my_car.get_model())
# print(my_car.get_speed())
# print(my_car.get_color())
# print(my_car.get_is_police())
# my_car.go()
# my_car.stop()
# my_car.turn()
#
#
# my_car = SportCar('Lamborgini')
# print(my_car.get_model())
# print(my_car.get_speed())
# print(my_car.get_color())
# print(my_car.get_is_police())
# my_car.go()
# my_car.stop()
# my_car.turn()
#
# my_car = PoliceCar('Ford')
# print(my_car.get_model())
# print(my_car.get_speed())
# print(my_car.get_color())
# print(my_car.get_is_police())
# my_car.go()
# my_car.stop()
# my_car.turn()



# 2

class Car:
    def __init__(self, car_model):
        self._model = car_model

    def get_model(self):
        return self._model

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self):
        print('Машина повернула')







class TownCar(Car):
    def __init__(self):
        self._speed = '90 км в час'
        self._color = 'Красная'
        self._is_police = 'Не полицейская машина'

    def get_speed(self):
        return self._speed

    def get_color(self):
        return self._color

    def get_is_police(self):
        return self._is_police

# lada = TownCar('Lada')



# my_car = TownCar()

my_car(TownCar)
# print(my_car.get_model())
# print(my_car.get_speed())
# print(my_car.get_color())
# print(my_car.get_is_police())
# my_car.go()
# my_car.stop()
# my_car.turn()

