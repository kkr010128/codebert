def to_fizzbuzz(num: int) -> str:
    if num % 15 == 0:
        return 'FizzBuzz'
    if num % 3 == 0:
        return 'Fizz'
    if num % 5 == 0:
        return 'Buzz'
    return str(num)


N = int(input())
answer = 0
for i in range(1, N + 1):
    fb_str = to_fizzbuzz(i)
    if fb_str.isdecimal():
        answer += int(fb_str)
print(answer)