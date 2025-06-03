# -*- coding: utf-8 -*-
import math

def prime_number_identifier(num):
    for candidate in range(2, int(math.sqrt(num)) + 1):
        if num % candidate == 0:
            return False
    return True


input_num = int(raw_input())
counter = 0
found_number = 0
while counter < input_num:
    candidate_number = int(raw_input())
    if prime_number_identifier(candidate_number):
        found_number += 1
    counter += 1

print found_number