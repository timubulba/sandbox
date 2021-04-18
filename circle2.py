#!/usr/bin/env python

count = 10000000
steps = 5

circle = [i +1  for i in range(count)]
circle[count - 1] = 0

prev = 0

cur = 0
while cur != circle[cur]:
    for i in range(5):
        prev = cur
        cur = circle[cur]
    cur = circle[prev] = circle[cur]
print(cur)