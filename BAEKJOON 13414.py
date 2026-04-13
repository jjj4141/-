import sys
input = sys.stdin.readline
waiting_dict = {}

l, k = map(int, input().split())

for i in range(k):
    student_id = input().rstrip()
    waiting_dict[student_id] = i

result = sorted(waiting_dict.keys(), key = lambda x: waiting_dict[x])

print("\n".join(result[:l]))
