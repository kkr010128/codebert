a, b, c , d = map(int, input().split())

M = b * d;
if M < a * c:
    M = a*c;
if M < b * c:
    M = b*c;
if M < a * d:
    M = a * d;
    

print (M);