# 📝 [10870] 피보나치 수5

def fibo(N):
    if N <= 1:
        return N
    return fibo(N-1) + fibo(N-2)	# 앞 두 수의 합

N = int(input())
print(fibo(N))