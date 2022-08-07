import random

# create a number randomly from random module
number = random.randrange(100)

# defining a while loop for finding the number
# but this time you only have 3 rights
count = 0
while count < 3:
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

    count += 1

    if count == 3:
        print('Sorry! You could not guess the nuber...')
