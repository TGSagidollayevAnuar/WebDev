n = int(input())
a = []
for i in range(0, n):
    a.append(int(input()))
for i in range(0, n):
    if (a[i] > 0 and a[i+1] > 0) or (a[i] < 0 and a[i+1] < 0):
        print(a[i], a[i+1])
        break