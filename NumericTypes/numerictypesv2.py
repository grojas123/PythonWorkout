def guessing_game():
    import random
    answer = int(random.randint(1, 100))
    print(answer)
    while True:
        user_guess = int(input("What is your guess? "))
        if user_guess == answer:
            print(f'Right! The answer is {user_guess}')
            break
        if user_guess < answer:
            print(f'Your guess of {user_guess} is too low!')
        else:
            print(f'Your guess of {user_guess} is too high!')
guessing_game()