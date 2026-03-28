n = int(input())

if (n == 1):
    print("*")

else:

    for i in range(n):

        if (i % 2 != 0):
            print(("* " * ((n + 1) // 2)).rstrip())
            
        else:
            print(" *" * (n // 2))
