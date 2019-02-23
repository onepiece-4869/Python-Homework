import random

num = random.randint(1,10)

guess = int(input('Guess a number between 1 and 10\n'))

while guess != num:
    guess = int(input('Guess agagin\n'))
else:
    print(input('You Win!'))