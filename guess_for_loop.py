import random

# create a number randomly from random module
number = random.randrange(100)

# defining a for loop for finding the number. for loop is a little bit more reliable way to avoid infinite loop
# you only have 3 rights
count = 0
for i in range(3):
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
