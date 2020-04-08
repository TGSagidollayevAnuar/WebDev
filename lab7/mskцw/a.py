import math
n = int(input())
i = 0
while i != n:
    i += 1
    if math.sqrt(i) % 1 == 0:
        print(i)
