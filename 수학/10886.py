# 📝 [10886] 0 = not cute / 1 = cute

n = int(input())
a = 0
b = 0

for i in range(n):
    k = int(input())
    if k == 0:
        b += 1
    else:
        a += 1

if a > b:
    print("Junhee is cute!")