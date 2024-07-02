# 📝 [10799] 쇠막대기
# 쇠막대기는 여러개가 겹쳐져 있지만 시작점이나 끝점이 같은 경우는 없고 위에 쇠막대기는 무조건 아래 쇠막대기 보다 짧다.
# 레이저도 쇠막대기 끝점과 겹치지 않는다.
# stack을 써서 저장해 나가는데 시작 점 ( 은 나올 때 마다 레이저인지 확인해 주어야 하고 끝 점 ) 은 나올 때 마다 조각이 잘려진다고 생각한다.

lst = input()
total = 0  
pre = 0  
stack = []
for l in lst:
    if l == '(':
        stack.append(l)
    elif l == ')' and pre == '(':  
        stack.pop()  
        total += len(stack)  
    else: 
        stack.pop()  
        total += 1
    pre = l  
print(total)