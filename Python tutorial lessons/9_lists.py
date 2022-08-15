#Lists

#names = ['John', 'Bob', 'Aaron', 'Sarah', 'Mary']
#names[0] = 'Jon'
#print(names[2:])
#print(names)

numbers = [3, 6, 2, 8, 4, 10]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)