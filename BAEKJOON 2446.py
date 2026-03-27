n = int(input())

for i in range(1, 2*n):
    print(" " * ((n-1) - abs(n - i)) + "*" * (1 + abs(2*n -2 - (i-1)*2)))
