# 📝 [1343] 폴리오미노

N = input()

N = N.replace("XXXX", "AAAA")
N = N.replace("XX", "BB")

if 'X' in N:
    print(-1)
    
else:
    print(N)