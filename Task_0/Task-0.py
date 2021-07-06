#Виконав студент групи Ki-20010б Муха Віталій
import random
randomlist = random.sample(range(-100, 100), 30)
print(randomlist)
print("\nМаксимальний елемент списку: ", max(randomlist)) #
print("Його порядковий номер: ", randomlist.index(max(randomlist)))
newlist = [i for i in randomlist if (i % 2) == 1]
if len(newlist) == 0:
    print("Таких чисел немає!")
print(sorted(newlist, reverse=True))
print("\n")