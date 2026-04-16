def d(n):
    total = 0
    for i in range(1, n+1):
        if (i < 100):
          total += 1
        else:
            is_hansu = True
            a = len(str(i))
            num = list(map(int, str(i)))
            for u in range(a-2):
                if num[u] - num[u+1] != num[u+1] - num[u+2]:
                    is_hansu = False
                    break
                
            if is_hansu:
                total += 1
    return total

n = int(input())
print(d(n))
