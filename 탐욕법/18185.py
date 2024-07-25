# 📝 [18185] 라면사기 (small)

import sys
input = sys.stdin.readline

n = int(input())
ans,cnt=0,0
arr = [0 for _ in range(100000)]

buf = list(map(int, input().split()))

for i in range(len(buf)):
    arr[i] = buf[i]
    
for i in range(n):
    
    if arr[i+1]>arr[i+2]:
        cnt = min(arr[i], arr[i+1]-arr[i+2])
        ans += 5*cnt
        arr[i]-=cnt; arr[i+1]-=cnt

        cnt2 = min(arr[i], min(arr[i+1], arr[i+2]))
        ans+=7*cnt2
        arr[i]-=cnt2; arr[i+1]-=cnt2; arr[i+2]-=cnt2;
    
    else: 
        cnt2 = min(arr[i], min(arr[i+1], arr[i+2]))
        ans+=7*cnt2
        arr[i]-=cnt2; arr[i+1]-=cnt2; arr[i+2]-=cnt2;
        
        cnt = min(arr[i], arr[i+1])
        ans += 5*cnt
        arr[i]-=cnt; arr[i+1]-=cnt
       
    ans += 3*arr[i]
print(ans)