n = int(input())
Taro = 0
Hanako = 0

for i in range(n):
    x = 0
    t,h = input().split()
    for j in range(min(len(t),len(h))):
        if t == h:
            Hanako += 1
            Taro += 1
            x = 1 
            break
        if ord(t[j:j+1]) > ord(h[j:j+1]):
            Taro += 3
            x = 1
            break
        if ord(t[j:j+1]) < ord(h[j:j+1]):
            Hanako += 3
            x = 1
            break
    if x == 0:
        if len(t) > len(h):
            Taro += 3
        elif len(t) < len(h):
            Hanako += 3
	

print("{} {}".format(Taro,Hanako))