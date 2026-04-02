step = list(map(int, input().split()))

step.remove(max(step))

print(max(step) * min(step))
