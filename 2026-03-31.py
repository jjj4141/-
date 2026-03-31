month_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
firstDay=4
n = int(input())
for i in range(12):
    if n == i+1:
        break
    firstDay+=month_day[i]
firstDay=firstDay%7
list=[]
for j in range(month_day[n-1]):
    if j <9:
        t=" "+str(j+1)
        list.append(t)
    else:
        list.append(j+1)
for firstWeek1 in range(firstDay):
    list.insert(0, "  ")
#for k in range(list):
#    if 
print(list[-1])
print("         ",n,"월", sep='')
print("일 월 화 수 목 금 토")
for k in range(list[-1]//7+2):
    print(*list[0:7])
    del list[0:7]
  
