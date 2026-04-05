n = int(input())

for _ in range(n):
    answer = input()
    is_vps = "YES"
    data = []

    for i in answer:
        if (i == "("):
            data.append(i)

        else:
            if data:
                data.pop()

            else:
                is_vps = "NO"
                break

    if data:
        is_vps = "NO"

    print(is_vps)
