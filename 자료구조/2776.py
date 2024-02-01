# 📝 [2776] 암기왕

for _ in range(int(input())):

    a = int(input())
    su1 = set(map(int, input().split()))
    
    b = int(input())
    su2 = list(map(int, input().split()))
    
    for n in su2:
        print(1 if n in su1 else 0)