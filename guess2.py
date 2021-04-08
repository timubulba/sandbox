#!/usr/bin/env python


print("Think of a number, I'll guess it")

left = 1
right = 100

while True:
    print(f'{left} {right}')
    if left > right:
        print('You are cheating!')
        break
    if left == right:
        print(f"I know your number! It's {left}")
        break
    mid = (left + right) // 2
    answer = input(f'Is it {mid}? ')
    if answer == '<':
        right = mid - 1
    elif answer == '>':
        left = mid + 1
    elif answer == '=':
        break
    else:
        print('Incorrect input. Try > < =')
