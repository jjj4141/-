d = 4
t = 0
n = int(input())

for i in range(n):
    d = d*4 - (4*(2**t)) - 3
    t += 1

print(d)
