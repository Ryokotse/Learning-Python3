#List methods

#numbers = [5, 2, 1, 5, 7, 4]
#print(50 in numbers)
#print(numbers.sort())
#print(numbers)
#numbers2 = numbers.copy()
#numbers.append(10)
#numbers.reverse()
#print(numbers2)

numbers = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)