n=int(input())
print(*[chr(65+(ord(a)+n-65)%26) for a in input()], sep='')