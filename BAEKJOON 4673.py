def d(n):
   return n + sum(map(int, str(n)))

all_numbers = set(range(1,10001))
generated_numbers = set()

for i in range(1, 10001):
   if d(i) <= 10000:
      generated_numbers.add(d(i))

result = sorted(list(all_numbers - generated_numbers))

print('\n'. join(map(str, result)))
