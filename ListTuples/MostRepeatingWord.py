from collections import Counter
def mostRepeatingWord(words):
    list_counts=[]
    for word in words:
        list_counts.append(Counter(word).most_common())

    return list_counts

words = ['this', 'is', 'an', 'elementary', 'test', 'example']
print(mostRepeatingWord(words))