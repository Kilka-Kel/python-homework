#
text = 'съешь ещё этих мягких французских булок'
print(len(text)) # Кол-во символов
print('ещё' in text) # Проверить включает ли строка слово
print(text.isdigit()) # Являются ли все символы в строке числами
print(text.islower()) # Являются ди все символы в строке символами нижнегго регистра
print(text.replace('ещё','ЕЩЁ')) # Если мы что-то хотим заменить

# for c in text:
#  print(c)

# help(text.islower)# Запросить подсказку по тому или иному методу

print(text[0]) # c
print(text[1]) # ъ
print(text[len(text)-1]) # к - Вывести последний
print(text[-5]) # б
print(text[:]) # print(text) то же что text[0:len(text)-1]
print(text[:2]) # съ то же что text[0:2
print(text[len(text)-2:]) # ок
print(text[2:9]) # ешь ещё
print(text[6:-18]) # ещё этих мягких
print(text[0:len(text):6]) # сеикакл  - берёт каждый 6 символ
print(text[::6]) # сеикакл
text = text[2:9] + text[-5] + text[:2] # ...
print(text)

numbers = [1, 2, 3, 4, 5]
print(numbers) # [1, 2, 3, 4, 5]
#
ran = range(1, 6)
print (type(ran))
numbers = list(ran)
#  То же что numbers = list(range(1,6))
print (type(numbers))
#

print(numbers) # [1, 2, 3, 4, 5]
print (len(numbers), ' len')
numbers[0] = 10
print(numbers) # [10, 2, 3, 4, 5]
#

for i in numbers:
 i *= 2
 print(i) # [20, 4, 6, 8, 10]
print(numbers) # [10, 2, 3, 4, 5] 
# после печати список возвращает свои значения 


#Вы должны использовать exit()команду в окне интерпретатора python, чтобы завершить сеанс python.

colors = ['red', 'green', 'blue']
for e in colors:
 print(e) # red green blue
for e in colors:
 print(e*2) # redred greengreen blueblue
colors.append('gray') # добавить в конец
print(colors == ['red', 'green', 'blue', 'gray']) # True
colors.remove('red') #del colors[0] # удалить элемент


# def f(x):
#  return x**2
def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

arg = 2
print (f(arg))
print (type(f(arg)))