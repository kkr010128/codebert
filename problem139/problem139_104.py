def study_time(h1, m1, h2, m2, k):
    result = (h2 - h1) * 60 + m2 - m1 - k
    return result

h1, m1, h2, m2, k = tuple(map(int, input().split()))

if __name__ == '__main__':
    print(study_time(h1, m1, h2, m2, k))