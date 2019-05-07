############
### EASY ###
############

# 1
a = 10
b = 'word'
c = input('Введите, чего душа пожелает: ')
print(a)
print('Значение переменной a: ' + str(a))
print('Значение переменной b: ' + b)
print('Введенное Вами значение: ' + c)


# 2
number = int(input('Введите число:'))
number += 2
print('К введенному числу прибавили 2. Получилось: ' + str(number))


# 3
age = int(input('Введите Ваш возраст: '))
if age >= 18:
    print('Доступ разрешен')
else:
    print('Извините, пользование данным ресурсом только с 18 лет')


##############
### MEDIUM ###
##############

# 1
number = int(input('Введите число от 2 до 10:'))
while (number < 2) or (number > 10):
    number = int(input('Введите число от 2 до 10:'))
else:
    number = number ** 2
    print(number)

# 2
number1 = int(input('Введите первое число:'))
number2 = int(input('Введите второе число:'))

if number1 > number2:
    number1 = number1 - number2  # Находим разницу. Присваиваем number1
    number2 = number1 + number2  # К значению number2 прибавляем разницу
    number1 = number2 - number1  # из number2 вычитаем разницу
else:
    number2 = number2 - number1  # находим разницу
    number1 = number2 + number1  # к значению number1 прибавляем разницу
    number2 = number1 - number2  # из number1 вычитаем разницу

print('Первое число: ' + str(number1))
print('Второе число: ' + str(number2))



############
### HARD ###
############

#1
print('Добро пожаловать в нашу клинику!')
print('Для заполения медицинской карты необходимо ввести некоторые данные.')
surname = input('Введите Вашу фамилию: ')
name = input('Имя: ')
age = int(input('Возраст (полных лет):'))
weight = int(input('Вес: '))

if age < 30 and (weight >= 50 and weight < 120):
    print('Вы полностью здоров!')
elif age > 30 and (weight < 50 or weight > 120):
    print('Вам требуется начать вести правильный образ жизни.')
elif age > 40 and (weight < 50 or weight > 120):
    print('Вам требуется врачебный осмотр.')
else:
    print('Клиент - неведомое существо.')
