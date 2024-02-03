# 📝 [5347] LCM
# 두 수의 최소공배수를 구하기

N = int(input())

def gcd(a, b):
    while b:
        mod = b
        b = a % b
        a = mod
    return a

for _ in range(N):
    a, b = map(int, input().split())
    print(a*b//gcd(a, b))
    