#!/usr/bin/env python

count = 100000
steps = 5

circle = [i for i in range(count)]

i = 0

while len(circle) > 1:
    i += steps
    i %= len(circle)

    #print(circle[i])
    del(circle[i])

print(circle)