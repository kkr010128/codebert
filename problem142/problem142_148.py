n = str(input())
print('hon' if (int(n[len(n)-1]) in {2, 4, 5, 7, 9}) else 'pon' if (int(n[len(n)-1]) in {0, 1, 6, 8}) else 'bon' )