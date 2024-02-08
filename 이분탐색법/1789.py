# 📝 [1789] 수들의 합

N = int(input())

sum=0
result=0

for i in range(1, N+1):
  sum += i
  result += 1
  if sum > N:
    result -= 1
    break
    
print(result)