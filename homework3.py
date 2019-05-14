############
### EASY ###
############

# 1
# def anketa(name, age, city):
#     print(name + ', ' + str(age), 'год(а), проживает в городе', city + '.')
# name = input('Введите имя: ')
# age = int(input('Введите возраст: '))
# city = input('Введите город проживания: ')
# anketa(name, age, city)


# 2
# def max_number(list):
#     print('Максимальное число: ', max(list))
# list = (10,5,2)
# max_number(list)


# 3
# def max_string(*args):
#     print(max(args, key=len))
# max_string('Hello_World','Show_Must_Go_On','Python_rules')



##############
### NORMAL ###
##############

# 1

names = ('Alex', 'Sergey', 'Ivan', 'Pert', 'Nikolay')
salary = (150000, 75000, 200000, 135000, 600000)
my_dictionary = dict(zip(names, salary))
print(my_dictionary)


file = open('homework3.txt', 'w')
for i in my_dictionary:
    # print(i, '-', my_dictionary[i])
    key = i
    value = my_dictionary[i]
    file.write(str(key))
    file.write(' - ')
    file.write(str(value))
    file.write('\n')
file.close()

# with open('homework3.txt') as file:
#     for line in file:
#         # print(line, end='')
#         line.split(' ')

