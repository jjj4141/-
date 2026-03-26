n = input()
i = "100"
t = 0

if (len(n) == 1):
    n = "0" + n

while (int(n) != int(i)):
    if (t == 0):
        a = str(int(n[0]) + int(n[1]))

        if (len(a) == 1):
            i = n[1] + a

        else:
            i = n[1] + a[-1]

    else:
        a = str(int(i[0]) + int(i[1]))

        if (len(a) == 1):
            i = i[1] + a

        else:
            i = i[1] + a[-1]

    t += 1

print(t)
