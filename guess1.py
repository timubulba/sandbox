#!/usr/bin/env python

import random

print('I thought of a number, guess it!')

n = random.randrange(1, 100, 1)
while True:
    s = input('> ')
    a = int(s)
    if a == n:
        print('You guessed right!')
        break
    elif a < n:
        print('Too low')
    else:
        print('Too hight')
