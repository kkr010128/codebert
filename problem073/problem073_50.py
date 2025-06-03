from math import sqrt

# Function to return count of Ordered pairs
# whose product are less than N
def countOrderedPairs(N):
    # Initialize count to 0
    count_pairs = int(0)

    # count total pairs
    p = int(sqrt(N - 1)) + 1
    q = N
    # q = int(sqrt(N)) + 2
    for i in range(1, p, 1):
        for j in range(i, q, 1):
            if i * j > N-1:
                break
            # print(i,j)
            count_pairs += 1
    #print(count_pairs)
    # multiply by 2 to get ordered_pairs
    count_pairs *= 2

    #print(count_pairs)
    # subtract redundant pairs (a, b) where a==b.
    count_pairs -= int(sqrt(N - 1))

    # return answer
    return count_pairs

    # Driver code

N = int(input())
print(countOrderedPairs(N))
# ans=prime_factorize(N)
# print(ans)