N = int(input())
numbers = [int(input()) for i in range(N)]
ans = []

def check_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return 0
    else:
        return 1
    
for n in numbers:
    ans.append(check_prime(n))

print(sum(ans))