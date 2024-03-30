def firstlast(collection):
    return collection[0], collection[len(collection) - 1]
print(firstlast("Hello World"))
print(firstlast([1,2,3]))
print(firstlast((1,2,4)))