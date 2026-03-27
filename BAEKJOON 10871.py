n, x = map(int, input().split())
a = list(input().split())[:n]
r = list()

for i in range(len(a)):
    if (int(a[i]) < x):
        r.append(a[i])

print(*r)
