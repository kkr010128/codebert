import math

def main():
    a,b,c = map(int,input().split())
    left = 4*a*b
    right = (c-a-b)**2
    if (c-a-b)<0:
        return 'No'

    if left < right:
        return 'Yes'
    else:
        return 'No'

print(main())
