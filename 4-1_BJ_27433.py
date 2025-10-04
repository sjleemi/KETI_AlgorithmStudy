# 4주차 재귀 27433번
# 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

def getfact(N):
  if N <= 1 :
    return 1
  else :
    return N * getfact(N-1)

print(getfact(N))
