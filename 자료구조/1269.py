# 📝 [1269] 대칭 차집합

n, m = map(int, input().split())

aset = set(map(int, input().split()))
bset = set(map(int, input().split()))

print(len(aset - bset) + len(bset - aset))