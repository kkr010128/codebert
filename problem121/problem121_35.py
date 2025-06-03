n=int(input())

abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
ans = ''
while n:
    ans += abc[(n-1)%len(abc)]
    n = (n-1)//len(abc)
print(ans[::-1])
