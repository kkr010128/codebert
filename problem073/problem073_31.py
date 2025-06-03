# Python3 implementation of the approach
# Function to find the number of divisors
# of all numbers in the range [1,n]
def findDivisors(n):
    # List to store the count
    # of divisors
    div = [0 for i in range(n + 1)]

    # For every number from 1 to n
    for i in range(1, n + 1):

        # Increase divisors count for
        # every number divisible by i
        for j in range(1, n + 1):
            if j * i <= n:
                div[i * j] += 1
            else:
                break

    # Print the divisors
    return div

    # Driver Code


if __name__ == "__main__":
    n = int(input())
    print(sum(findDivisors(n-1)))

# This code is contributed by
# Vivek Kumar Singh
