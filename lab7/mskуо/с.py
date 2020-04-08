a = str(input())
b = int(input())

if (len(a) == 4 and a[0] == a[len(a)-1] and a[1] == a[len(a)-2] and b == 1) or (len(a) != 4 and b != 1) or (len(a) == 4 and a[0] != a[len(a)-1] and b != 1):
    print('YES')
elif (len(a) == 4 and a[0] == a[len(a)-1] and a[1] == a[len(a)-2] and b != 1) or (len(a) != 4 and b == 1) or (len(a) == 4 and a[0] != a[len(a)-1] and b == 1):
    print('NO')


