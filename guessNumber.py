    import random
answer = random.randint(1, 10)
print(answer)
while True:
    try:
        guess = int(input('Guess a number between 1 and 10: '))
        if 0 < int(guess) < 11:
            if int(guess) == answer:
                print('you are a genius')
                break
    except ValueError:
        print('please enter a number')
        continue
