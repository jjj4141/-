m = int(input())
n = int(input())

prime_number = [True] * (n + 1)
prime_number[0] = prime_number[1] = False

for i in range(2, n+1):
    if (prime_number[i] == True):
        for u in range(i * i, n + 1, i):
            prime_number[u] = False

result = []
for i in range(m, n + 1):
    if (prime_number[i]):
        result.append(i)

if result:
    print(sum(result))
    print(min(result))

else:
    print("-1")
