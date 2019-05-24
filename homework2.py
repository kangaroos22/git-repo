############
### EASY ###
############

# 1
fruits = ["Яблоко", "Банан", "Киви", "Арбуз"]
i = 0
for n in fruits:
    i += 1
    print(str(i) + '. ' + '{:>6}'.format(n))


# 2
list_src = [32, 55, 76, 432, 767, 77, 13, 54]
list_dst = []
for n in list_src:
    if n % 2 == 0:
        n = n / 4
        list_dst.append(n)
    else:
        n = n * 2
        list_dst.append(n)
print(list_src)
print(list_dst)




##############
### NORMAL ###
##############

# 1
import random

list_src = []
list_dst = []

i = 0

while i < 50:
    list_src.append(random.randint(4, 100))
    i += 1

for n in list_src:
    x = n ** 0.5
    if int(x) == float(x):
        #print(list_src.index(n), n, x)
        #print(x)
        #print(str(list_src.index(n)) + ' элемент: ' + str(n) + '. Его корень: ' + str(int(x)))
        print('{:>2}'.format(str(list_src.index(n))) + ' элемент: ' + '{:>3}'.format(n) + '. Его корень: ' + str(int(x)))
        list_dst.append(int(x))

print(list_src)
print(list_dst)



# 2
date = "02.11.2013"
date = input('Введите дату в формате дд.мм.гггг: ')
day, month, year = date.split('.')
print(day, month, year)

list_day = {'01':'Первое', '02':'Второе', '03':'Третье', '04':'Четвертое', '05':'Пятое', '06':'Шестое', '07':'Седьмое',
            '08':'Восьмое', '09':'Девятое', '10':'Десятое', '11':'Одиннадцатое', '12':'Двеннадцатое',
            '13':'Тринадцатое', '14':'Четырнадцатое', '15':'Пятнадцатое', '16':'Шестнадцатое', '17':'Семнадцатое',
            '18':'Восемьнадцатое', '19': 'Девятнадцатое', '20':'Двадцатое', '21':'Двадцать первое',
            '22':'Двадцать второе', '23':'Двадцать третье', '24':'Двадцать четвертое', '25':'Двадцать пятое',
            '26':'Двадцать шестое', '27':'Двадцать седьмое', '28':'Двадцать восьмое', '29':'Двадцать девятое',
            '30':'Тридцатое', '31':'Тридцать первое'}
list_month = {'01': 'января', '02': 'февраля', '03': 'марта', '04': 'апреля', '05': 'мая', '06':'июня', '07':'июля',
              '08':'августа', '09':'сентября', '10':'октября','11':'ноября','12':'декабря'}
print(list_day[day], list_month[month], year + ' года.')


# 3
import random

count = int(input('Введите количество элеметов в листе: '))
list_src = []
n = 0
while n < count:
    list_src.append(random.randint(-100, 100))
    n += 1
print(list_src)


# 4
i = 0
x = 0
lst = [1, 2, 4, 5, 6, 2, 5, 2]
lst2 = []
lst3 = []

for n in lst:           # Неповторяющиеся элементы исходного списка
    if len(lst2) == 0:
        lst2.append(n)
    else:
        for m in lst2:
            # print(m)
            if n == m:
                x += 1
        if x == 0:
            lst2.append(n)
print(lst2)

# Не до конца...
for n in lst[i:]:       # элементы исходного списка, которые не имеют повторений
    print('Проход:', i, 'Значение:', n)
    i += 1
    x = 0
    for m in lst[i:]:
        if n == m:
            x += 1

            print('Есть повторения:', n)
    if x == 0:
        lst3.append(n)
    else:
        lst3.append(n)
print(lst3)




############
### HARD ###
############

# 1


# 2
date = input('Введите дату в формате дд.мм.гггг: ')
day, month, year = date.split('.')
# print(day, month, year)

while (int(day) < 1 or int(day) > 31) or (int(month) < 1 or int(month) > 12) or (int(year) < 1 or int(year) > 9999):
    print('Вы неправильно ввели день/месяц/год...')
    date = input('Введите дату в формате дд.мм.гггг: ')
    day, month, year = date.split('.')

# Указываем месяцы в значениях возможного количества дней
list_day = {28: [2],
            30: [4, 6, 9, 11],
            31: [1, 3, 5, 7, 8, 10, 12]}

for n in list_day:
    # print(list_day[n])        # Выводим содержимое индексов
    for m in list_day[n]:       # Считываем каждое значение индекса
        # print(m)
        if int(month) == m:     # Если число введенного месяца совпало с содержимым индекса...
            if int(day) > n:    # Проверяем введенный день с количеством дней в месяце
                print(n, 'дней в', int(month), 'месяце. Вы ввели -', day + '.')
                print('Попробуйте сначала.')
            else:
                print(date)