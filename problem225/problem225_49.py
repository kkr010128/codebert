def main():
 h,a = map(int,input().split())
 ans = h // a
 if h % a != 0:
     ans += 1
 print(ans)
main()