N = int(input())
A = list(map(int, input().split()))

even_numbers = [a for a in A if a % 2 == 0]

is_approved = all([even_num % 3 == 0 or even_num % 5 == 0 for even_num in even_numbers])

if is_approved:
    print('APPROVED')
else:
    print('DENIED')
