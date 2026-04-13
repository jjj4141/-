import sys
input = sys.stdin.readline


sold = {}
n = int(input())

for _ in range(n):
    book = input().rstrip()
    sold[book] = sold.get(book, 0) + 1

max_count = max(sold.values())
max_sold = [name for name, count in sold.items() if count == max_count]

print(min(max_sold))
