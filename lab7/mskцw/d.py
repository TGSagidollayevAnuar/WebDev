n = int(input())
i = 1
while i <= n:
    if i == n:
        break
    i *= 2
if i == n:
    print('YES')
else:
    print('NO')
