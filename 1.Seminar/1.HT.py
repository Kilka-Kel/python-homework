print ('1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.')

a = int(input('Введите цифру, обозначающую день недели- '))

if a  == 6:
 print('Суббота, тусим')
elif a == 7:
 print('Воскресенье')
elif a > 7:
 print('Это не номер дня недели')
else:
 print('Это не выходной', a)



print ('2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.')
# def vvod (q):
#     if q != 1 and q!=0:
#         print ('Введите значение равное 1 или 0')
x= None
while x == None:  
    x = int(input('Введите x - '))  
    if x != 1 and x!=0:
        print ('Введите значение равное 1 или 0')
        x= None
x = bool(x) 

y= None
while y == None:  
    y = int(input('Введите y - '))  
    if y != 1 and y!=0:
        print ('Введите значение равное 1 или 0')
        y= None
y = bool(y) 

z= None
while z == None:  
    z = int(input('Введите z - '))  
    if z != 1 and z!=0:
        print ('Введите значение равное 1 или 0')
        z= None
z = bool(z) 
first = not (x or y or z)
second = not x and not y and not z
check = first == second
print (' при заданных значениях, выражение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z принимает значение - ', check)


print ('4. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).')

x1= 0
while x1 == 0:  
    x1 = int(input('Введите x1 - '))  
    if x1 == 0:
        print ('Введите значение не равное 0')
        x1 = 0
x1 = (x1>0)

y1= 0
while y1 == 0:  
    y1 = int(input('Введите y1 - '))  
    if y1 ==0:
        print ('Введите значение не равное 0')
        y1= 0
x1 = x1>0

if x1 > 0:
    if y1 > 0:
        rez = 1
        print('номер четверти - ',rez, ' принимаемые значения: x > 0, y > 0')
    else:
        rez = 4
        print('номер четверти - ',rez, ' принимаемые значения: x > 0, y < 0')
elif y1 > 0:
     rez = 2
     print('номер четверти - ',rez, ' принимаемые значения: x < 0, y > 0')
else :
    rez = 3
    print('номер четверти - ',rez, ' принимаемые значения: x < 0, y < 0')



print ('4. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.')

ax = float(input('Введите координаты точки a по оси x:'))
ay = float(input('Введите координаты точки a по оси y:'))
bx = float(input('Введите координаты точки b по оси x:'))
by = float(input('Введите координаты точки b по оси y:'))

import math
distans = round(math.sqrt((ax-bx)**2+(ay-by)**2),2)
print ('Растояние между точкой A до точки B = ', distans)