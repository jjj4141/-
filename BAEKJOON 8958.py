n = int(input())

for u in range(n):
    answer = input()
    total = point = 1 if answer[0] == 'O' else 0

    for i in range(1, len(answer)):
        if (answer[i] == 'O'):
            point += 1
            total += point

        else:
            point = 0

    print (total)
