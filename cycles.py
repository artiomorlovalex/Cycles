#Циклы

for numbers in [9, 18, 27]: #Цикл for
    print(numbers)

#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

i = 5
while i < 1: #Цикл while
    print(i)
    i-- #Декремент

#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

for i in "785974860158649974589314438708937986181698516341583463560834653":
    if i == "6" or i == "2": #Цикл if(если)
        continue #Функция continue  начинает цикл заново, не задев остальную часть
    print(i, end='.') #Выводим символы, оставляя точки через одного

#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

for i in "Hello, user.":
    if i == "!":
        continue
    elif i == ",": #Цикл elif(если иначе)
        break #Функция break останавливает цикл, как только заметит запятую
    print(i)

#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

for i in "Привет, пользователь!":
    if i == "к":
        break
else:  #Цикл  else(иначе)
    print("В этой строке нету буквы к")

#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

for num in range(10):
       if num < 5:
         pass #Функция pass
       else:
         print(num)