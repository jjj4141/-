n = int(input())
t = 0

while (n >= 0):
    if (n % 5 == 0):
        t = t + (n // 5)
        print(t)
        break
    
    n -= 3
    t += 1

else:
    print("-1")
