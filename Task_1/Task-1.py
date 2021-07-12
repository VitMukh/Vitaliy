#Виконав студент групи Кі-20010б Муха Віталій
import re
string = input("\nВведіть будь-що: ")
letters = ''.join([i for i in string if not i.isdigit()])
nums = re.findall(r'\d+', string)
nums = [int(i) for i in nums]
print("\nРядок без чисел:", letters)
LetterS = ' '.join(word[0].upper() + word[1:-1] + word[-1:].upper() for word in letters.split())
print("Змінений рядок:", LetterS)
print("\nМасив чисел:", nums)
if len(nums) == 0:
    print("Масив не містить чисел, подальші операції не можуть бути проведені")
else:
    print("Максимальний елемент масиву:", max(nums))
    nums_with_index = [nums[i]**(i+1) for i in range(0, len(nums))]
    print("Масив чисел, піднесені до степеню по їх індексу:", nums_with_index)
print("\n")
