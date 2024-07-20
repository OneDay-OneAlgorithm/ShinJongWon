# 📝 [10162] 전자레인지

s = int(input())

if s % 10 != 0:
    print(-1)
else:
    A = B = C = 0
    A = s // 300
    B = (s % 300) // 60
    C = (s % 300) % 60 // 10
    print(A, B, C)