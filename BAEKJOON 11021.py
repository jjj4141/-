testcase = int(input())
casenumber = 1

for i in range(testcase):
    a, b = map(int, input().split())
    print("Case #", casenumber, ": ", a + b, sep="")
    casenumber +=1
