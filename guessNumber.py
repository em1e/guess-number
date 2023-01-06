import random
answer = random.randint(1, 10)
#print(f'Psst, rumor has it that {answer} is the answer')
while True:
    try:
        guess = int(input('Guess a number between 1 and 10: '))
        if 0 < int(guess) < 11:
            if int(guess) == answer:
                print('You are a genius!')
                break
            else:
              print('Wrong answer, try again')
    except ValueError:
        print('Please enter a number')
        continue
