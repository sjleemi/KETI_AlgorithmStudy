# 백준 19564

word = input()

K=1

for i in range (len(word)-1):
  if word[i]>=word[i+1]:
    K += 1

print(K)

