from itertools import accumulate

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    for _ in range(K):
        arr = [0]*(N+1)
        for i, a in enumerate(A):
            left = max(0, i-a)
            right = min(N, i+a+1)
            arr[left] += 1
            arr[right] -= 1
        
        A = list(accumulate(arr[:-1]))
        if all(a == N for a in A):
           break

    print(*A, sep=" ")



if __name__ == "__main__":
    main()