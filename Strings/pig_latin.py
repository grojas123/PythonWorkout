word='0123456789'
def pig_latin(word):
    if word[0] in 'aeiouAEIOU':
        return f'{word}way'
    return f'{word[1:]}{word[0]}ay'
print(pig_latin('rena'))