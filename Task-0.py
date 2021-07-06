import random
randomlist = random.sample(range(-100, 100), 30)
print(randomlist)
print("\nМаксимальний елемент списку: ", max(randomlist)) #знаходить і виводить максимальний елемент списку
print("Його порядковий номер: ", randomlist.index(max(randomlist))) #виводить порядковий номер максимального елемента списку

#Cписок, що складається тільки з непарних чисел вихідного списку
newlist = [i for i in randomlist if (i % 2) == 1]
if len(newlist) == 0: 
    print("Таких чисел немає!")
print(sorted(newlist, reverse=True)) #список, виведений в порядку зменшення елементів
print("\n")