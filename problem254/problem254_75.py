def main():
    s=set('123')
    a=int(input())
    b=int(input())
    s.remove(str(a))
    s.remove(str(b))
    print(s.pop())

main()
