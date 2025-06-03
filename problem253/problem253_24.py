import numpy as np

def min_steps_v2(n, a, b):
    n = np.int64(n)
    a = np.int64(a)
    b = np.int64(b)

    if (b - a) % 2 == 0:
        return np.int64(int(b - a) // 2)
 
    # odd case
    a_diff = a - 1
    b_diff = n - b
 
    if a_diff > b_diff:
      steps_to_even = n - b + 1
      remain_steps = min_steps_v2(n, a + (n - b) + 1, n)
    else:
      steps_to_even = a
      remain_steps = min_steps_v2(n, 1, b - a)
 
    return steps_to_even + remain_steps

numbers = input().split(' ')
 
n = int(numbers[0])
a = int(numbers[1])
b = int(numbers[2])
 
print(min_steps_v2(n, a, b))
