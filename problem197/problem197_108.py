def main():
    a,b,c = map(int,input().split(" "))
    if (c-a-b)**2 > a*b*4 and c > a + b:
        print("Yes")
    else:
        print("No") 
main()