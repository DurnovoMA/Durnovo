numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

count_numbers = len(numbers)
numbers_none = numbers.index(None)

sum_numbers = sum(numbers[:4] + numbers[4+1:])
average = sum_numbers/count_numbers

numbers[4] = average

print("Измененный список:", numbers)

