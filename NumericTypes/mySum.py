def mySum(*numbers):
    total=0
    if isinstance(numbers, tuple):
        if isinstance(numbers[0], list):
             for number in numbers[0]:
                 total = total + number
             return total
        else:
            for number in numbers:
                total = total + number
            return total
print(mySum(1,2,3,4,6))
print(mySum([1,2,3,4,5]))


