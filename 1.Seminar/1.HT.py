# print ('1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.')

# a = int(input('Введите цифру, обозначающую день недели- '))

# if a  == 6:
#  print('Суббота, тусим')
# elif a == 7:
#  print('Воскресенье')
# elif a > 7:
#  print('Это не номер дня недели')
# else:
#  print('Это не выходной', a)



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


# print (type(x) , x)
# print (type(y) , y)
# print (type(z) , z)
first = not (x or y or z)
second = not x and not y and not z
check = first == second

# print (first)
# print (second)

print (' при заданных значениях, выражение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z принимает значение - ', check)
