import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    print(10 - int(input()) // 200)
                    
if __name__ == '__main__':
    main()