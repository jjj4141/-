n = int(input())

data = list(map(int, input().split()[:n]))

result = sorted(data)

print(result[0], result[n-1])
