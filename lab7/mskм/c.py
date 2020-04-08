n = (int(input()))
a = []
c = 0
for i in range(0, n):
    a.append(int(input()))
for i in range(0, n):
    if a[i] > 0:
        c += 1
print(c)
