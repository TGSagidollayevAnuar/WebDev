maxi = 0
a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if a[i] > a[maxi]:
        maxi = i
print(a[maxi], maxi)