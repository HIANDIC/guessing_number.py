import random

# create a number randomly from random module
number = random.randrange(100)

# defining a while loop for finding the number
while True:
    # get a number from user
    guess = int(input('Enter a number between 0 and 100 : '))

    # defining a condition
    if guess > number:
        print('A little lower...')
    elif guess < number:
        print('A little higher...')
    else:
        print('You are mind reader')
        break
