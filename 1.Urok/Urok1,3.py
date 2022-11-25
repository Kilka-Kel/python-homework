# a = int (input('a='))

# b = int (input('b='))
# if a > b:
#     print ( 'a=',a,' больше b=',b)
# else:
#     print ( 'b=',b,' больше a=',a)

# username = input('Введите имя: ')
# if(username == 'Маша'):
#  print('Ура, это же МАША!');
# else:
#  print('Привет, ', username);


# username = input('Введите имя: ')
# if username == 'Маша':
#  print('Ура, это же МАША!')
# elif username == 'Марина':
#  print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#  print('Ильнар - топ)')
# else:
#  print('Привет, ', username)


# пересобираем инвертированое число
original = 2356
inverted = 0
while original != 0:
 inverted = inverted * 10 + (original % 10)
 original //= 10
#  print(original)
#  print(inverted)
else:
    print('ФСЁ')
print(inverted)

# Цикл for
for i in 1, 2, 3, 4, 5:
    print(i**2)
print('---')    
list = (1, 2, 3, 4, 5)
for i in list:
    print(i+1)
print('---')    
r = range(5) #range(5) Выдаёт набор/итератор который перечисляет от 0 до 5
for i in r:
    print(i)

print('то же что ')    
for i in range(5):
    print(i)
print('Можно указать диапазон от 1 до n-1')    
for i in range(1, 6):
    print(i)
    
print('Можно изменить шаг')    
for i in range(1, 10 , 2):
    print(i)

print('В качестве итерируемого объекта можно исп. строки')    
for i in 'qwer - ty':
    print(i)
# for i in 1, -2, 3, 14, 5:
# print(i)
# 1
# -2
# 3
# 14
# 5

r = range(5) # range(0, 5)
r = range(2, 5) # range(2, 5)
r = range(-5, 0) # range(-5, 0)
r = range(1, 10, 2) # range(1, 10, 2)
r = range(100, 0, -20) # range(100, 0, -20)
