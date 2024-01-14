# 📝 [18115] 카드 놓기
# 1. 제일 위의 카드 1장을 바닥에 내려놓는다.
# 2. 위에서 두 번째 카드를 바닥에 내려놓는다. 카드가 2장 이상일 때만 쓸 수 있다.
# 3. 제일 밑에 있는 카드를 바닥에 내려놓는다. 카드가 2장 이상일 때만 쓸 수 있다.

import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

N = int(input())

li = list(map(int, input().split()))
li.reverse()

dq = deque()
for i in range(N):
    if li[i] == 1:
        dq.appendleft(i + 1)
    elif li[i] == 2:
        dq.insert(1, i + 1) 
    elif li[i] == 3:
        dq.append(i + 1)

for i in dq:
    print(i, end=" ")
