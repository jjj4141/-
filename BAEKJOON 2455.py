f1, f2 = map(int, input().split())
s1, s2 = map(int, input().split())
t1, t2 = map(int, input().split())
fo1, fo2 = map(int, input().split())

a = f2 - s1 + s2
b = a - t1 + t2

r = [f1, a, b]
print(max(r))
