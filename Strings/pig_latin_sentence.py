
def pl_sentence(sentence):
    def pig_latin(word):
        if word[0] in 'aeiouAEIOU':
            return f'{word}way'
        return f'{word[1:]}{word[0]}ay'
    words = sentence.split(" ")
    translated_sentence = ""
    for word in words:
        translated_sentence= translated_sentence + pig_latin(word) + " "
    return translated_sentence

print(pl_sentence('this is a test translation'))