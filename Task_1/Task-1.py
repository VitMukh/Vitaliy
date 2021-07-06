#Виконав студент групи Кі-20010б Муха Віталій
import re
string = input("\nВведіть будь-що: ")
letters = ''.join([i for i in string if not i.isdigit()])
nums = re.findall(r'\d+', string)
nums = [int(i) for i in nums]
print("\nРядок без чисел:", letters)
print("Масив чисел:", nums)

LetterS = ' '.join(word[0].upper() + word[1:-1] + word[-1:].upper() for word in letters.split())
print("\nЗмінений рядок:", LetterS)
print("Максимальний елемент масиву:", max(nums))
nums.remove(max(nums))
nums_with_index = [nums[i]**i for i in range(0, len(nums))]
print("Масив чисел, піднесені до степеню по їх індексу:", nums_with_index)
print("\n")