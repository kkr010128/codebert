def skip_num(num_digits:list, compare_digit):
    compare_upper_digit = num_digits[compare_digit]
    compare_lower_digit = num_digits[compare_digit + 1]
    if compare_upper_digit > compare_lower_digit:
        num_digits[compare_digit + 1] = compare_lower_digit + 1
        if compare_digit + 2 > len(num_digits):
            num_digits[compare_digit + 2:] = [0] * (len(num_digits) - compare_digit - 2)
    else: # compare_upper_digit < compare_lower_digit
        num_digits[compare_digit] = compare_upper_digit + 1
        num_digits[compare_digit + 1:] = [0] * (len(num_digits) - compare_digit - 1)
    
    return int("".join([str(i) for i in num_digits]))

K = int(input())

lunlun_count = 0
num = 0
while True:
    num += 1
    if num < 10:
        lunlun_count += 1
    else:
        num_digits = list(map(int, str(num)))
        is_lunlun = True
        for i in range(len(num_digits) - 1):
            if abs(num_digits[i] - num_digits[i + 1]) > 1:
                is_lunlun = False
                num = skip_num(num_digits, i) - 1
                break
            
        if is_lunlun:
            lunlun_count += 1
    if lunlun_count >= K:
        break

print(num)
