def solution1():
    # https://www.youtube.com/watch?v=aRdGRrsRo7I 
    n = int(input())
    s = input()
    r, g, b = 0, 0, 0
    for i in s:
        if i == 'R': r += 1
        elif i == 'G': g += 1
        else: b += 1
    
    total = r*g*b
    # all permutations of rgb are valid, to check if s[i], s[j], s[k] is a permutation of 'rgb' we could use counter. Or neat trick: ASCII value of the sum of s[i] + s[j] + s[k] is same.

    is_rgb = ord('R') + ord('G') + ord('B')

    for i in range(n):
        for j in range(i+1, n):
            # Condition 2 fails when: i - j = k - j --> k = 2*j - i
            k = 2*j - i
            if k < n:
                if ord(s[i]) + ord(s[j]) + ord(s[2*j-i]) == is_rgb:
                    total -= 1
    print(total)

solution1()