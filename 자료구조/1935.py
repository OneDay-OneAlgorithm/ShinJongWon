# 📝 [1935] 후위표기식 2
# 계산 결과를 소숫점 둘째 자리까지 출력한다.

N = int(input())

str = input()
num_lst = [0]* N

for i in range(N):
    num_lst[i] = int(input())

stack = []

for i in str:			
    if 'A' <= i <= 'Z':
        stack.append(num_lst[ord(i)-ord('A')])
    else :	
        str2 = stack.pop()
        str1 = stack.pop()

        if i == '+':
            stack.append(str1+str2)
        elif i == '-':
            stack.append(str1-str2)
        elif i == '*':
            stack.append(str1*str2)
        elif i == '/':
            stack.append(str1/str2)

print('%.2f' %stack[0])	