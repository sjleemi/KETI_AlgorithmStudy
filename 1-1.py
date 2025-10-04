# 연습문제 1-1) 1부터 n까지 연속한 숫자의 제곱의 합을 구하는 프로그램(for 반복문 이용)

def sum(n):
  s=0
  for i in range (1,n+1):
    s=s+i*i
  return s


print(sum(10))


