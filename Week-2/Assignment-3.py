nlist = list(map(int, input().split()))

n = nlist[0]
a = nlist[1:]

maxValue = 0
maxCount = 0

for i in range(n):
    count = 0
    for j in range(n):
        if(a[j] == a[i]):
            count += 1
    if(count > maxCount):
        maxCount = count
        maxValue = a[i]
print(maxValue, end = "")
