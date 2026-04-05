n = int(input())
x = list(map(int, input().split()))
x.sort()
total = 0

for i in range(n):
    total += x[i] * ((i+1) - (n - i))

print(total * 2)
