import sys
input = sys.stdin.readline



n, m = map(int, input().split())
unheard = set()
unseen = set()

for i in range(n):
    unheard.add(input().rstrip())

for _ in range(m):
    unseen.add(input().rstrip())

unheard_unseen = unheard & unseen

result = sorted(list(unheard_unseen))

print(len(result))

for u in result:
    print(u)
