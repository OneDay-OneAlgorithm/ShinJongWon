# 📝 [10546] 배부른 마라토너

import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
dic = {}
for i in range(N):
    name = input()
    dic[name] = dic.get(name, 0) + 1

for i in range(N-1):
    name = input()
    dic[name] -= 1

dic_list = list(dic.items())
dic_list.sort(key = lambda x : (-x[1], x[0]))
print(dic_list[0][0])
