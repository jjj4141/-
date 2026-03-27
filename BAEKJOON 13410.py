n, k = map(int, input().split())
data = list()

for i in range(1,k+1):
    data.append(str(n*i)[::-1])

print(max(map(int, data)))
