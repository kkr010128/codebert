# -*- coding: utf-8 -*-

while True:
    deck = str(raw_input())
    if deck == '-':
        break
    m = int(raw_input())
    for i in range(m):
        h = int(raw_input())
        deck = deck[h:] + deck[0:h]
    print deck