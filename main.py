amount = int(input("Enter the amoun items: "))
items_type = input("Enter the amoun items: ")

try:
    amount = int(input("Enter amoun items: "))
    items_type = input("Enter the type items: ")
except:
    print("error")

for i in range(10):
    print("do smth in program")

# ////////////////////////////////////////////////////

try:
    amount = int(input("Enter amoun items: "))
    items_type = input("Enter the type items: ")

    l = [1,2,3]
    print(l[10])

    print(1 / 0)
except (ValueError, ZeroDivisionError, IndexError):
    print("ValueError, ZeroDivisionError, IndexError"):

















































напишіть програму яка дозволяє користувачеві обчислити частку (ділення одного числа на інше) двох чисел. програма приймає два    значення з клавіатури і повертає результат операції на екран. обговоріть виняток, що виникає під час ділення на нуль, і виведіть повідомленя про помилку
pyton


реалізуйте перше завдання через функцію. функція повинна приймати два параметри два параметри і відображати результат ділення на екран. створіть дві версії реалізаї функції
перша версія не обробляє виняток усередині функції. уся обробка знаходиться зовні
друга версія обробляє виняток усередині функції
 pyton

пишіть програму яка дає змогу заповнити користувачеві словник із клавіфтури парами "ключ/значення". після отримання даних відобразіть на екрані меню, яке дозволяє виконати  такі операції:
відображення словника, пошук значення в словнику. значення має бути знайдено за ключем
відображення значення за ключем введеним користувачем
видалення значення за ключем введеним користувачем
обробіть виняток що виникає під час виходу за межі словника (користувач ввів невірний ключ) і виведіть повідомлення про помилку