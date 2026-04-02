n = int(input())

for i in range(n):
    point = list(map(int, input().split()))
    scores = point[1:]
    average = sum(scores) / point[0]
    total = 0

    for u in scores:
        if (u > average):
            total += 1

    ratio = (total / point[0]) * 100
    print(f"{ratio:.3f}%")
