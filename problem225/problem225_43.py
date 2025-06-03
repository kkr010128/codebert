#Take input separated by space(?)
h,a = map(int, input().split())

#Divide, just round off and add 1 if decimal
hit = round(h//a)

if h%a != 0:
    hit = hit + 1

print(hit)
