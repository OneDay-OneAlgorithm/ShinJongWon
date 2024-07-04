# 📝 [4358] 생태학

import sys

total = 0
dic = dict()
while 1:
    word = sys.stdin.readline().rstrip()
    if word == '':
        break
    total += 1   
    if word in dic:   # 전에 이미 나왔으면
        dic[word] += 1
    else:
        dic[word] = 1
sdic = dict(sorted(dic.items()))
for i in sdic:
    a = sdic[i]
    per = (a / total * 100)
    
    print("%s %.4f" %(i, per))