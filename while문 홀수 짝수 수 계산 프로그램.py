
#while문 홀수 짝수 수 계산 프로그램
a = int(input("숫자를 입력해 주세요"))
b = 0
even = 0
odd = 0

while a>=b:
  b+=1
  if b%2 == 1:
    even+=1

  else:
    odd += 1

print("짝수:", even)
print("홀수:", odd)
