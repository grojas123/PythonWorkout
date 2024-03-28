#This solution didnt work
def mySum(*numbers):
    output=0
    for number in numbers:
        output=output+number
    return output
print(mySum(1,2,3,4,6))
print(mySum([1,2,3,4,5]))


