def guessing_number():
    import random
    lucky = False
    name = input("Enter your name: ")
    print(f'Hello {name}!')
    while not lucky:
        random_number = random.randint(1, 100)
        print("random number",random_number)
        guess_number=input('Enter your guess number : ')
        lucky = random_number == int(guess_number)

guessing_number()