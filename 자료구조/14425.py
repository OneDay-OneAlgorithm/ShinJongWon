# 📝 [14425] 문자열 집합

import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
ans = 0
dic = {}
for i in range(N):
    a = input()
    dic[a] = 1
for i in range(M):
    a = input()
    if a in dic:
        ans += 1
print(ans)