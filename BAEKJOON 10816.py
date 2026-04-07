import sys
input = sys.stdin.readline


n = int(input())
data = list(map(int, input().split()))
card_number = data[:n]

count_dict = {}
for i in card_number:
    if i in count_dict:
        count_dict[i] += 1

    else:
        count_dict[i] = 1

m = int(input())
question = list(map(int, input().split()))
answer = []

for u in question:
    answer.append(count_dict.get(u, 0))

print(*answer)
