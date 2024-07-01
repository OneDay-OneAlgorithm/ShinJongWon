# https://www.acmicpc.net/problem/3986
# 📝 [3986] 좋은 단어

import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
ans = 0
for i in range(N):
    stack = []
    a = input()
    for i in a:
        if not stack:
            stack.append(i)
        else:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
    if not stack:
        ans += 1
print(ans)