print ('Hello world')



a = 123
b = 1.5
value = None
print(type(value))

print (a)
print (b)

value= 'Newermore'
print (value)

# print(type(a))
# print(type(b))
# print(type(value)) # комментарий
c = 'Mutter'

print ('Hello World') # можно использовать одинарные ковычки
print ("Hello World") # А можно двойныеё
print ('Hello "World') # Если использовать одинарные, то можно в текст добавить двойную ковычку
print ("Hello 'World") # и наоборот 
print ('Hello \'World') # Можно воспользоваться так называемыми Escape-последовательности
print ("Hello \"World") 
print ('Hello \nWorld') # переход на новую строку


print (a,'-',b,'-',c) #Немного об интерполяциях
print ('{} - {} - {}'.format(a, b, c)) #форматированный вывод
print (f'{a} - {b} - {c}') #интерпаированый вывод
print ('{2} - {0} - {1}'.format(a, b, c)) #если надо поменять последоветельность


list = [1,2,3,4,5,'wasd']# можно держать в списке данные с разным итпом но НЕ СТОИТ ЭТОГО ДЕЛАТЬ
print(list)



f = True
print (f)
f = False
print (f)

list = [1,2,3]
print (list)
list2 = ['a', 'b', 'c']
print (list2)
list3 = ['a', 1 , 'b', 2.2 ,'c', True] # но лучше так не делать
print (list3)