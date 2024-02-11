# 📝 [2417] 정수 제곱근

N = int(input())

s = 0
e = N

while s <= e:
    mid = (s + e)  // 2
    if mid ** 2 < N:
        s = mid + 1
    else:
        e = mid -1

print(s)