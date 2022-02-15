
#if문 bmi 계산 프로그램
cm= int(input("키"))

kg= int(input("몸무게"))

m= cm/100

bmi= int(kg//m**2)

if bmi<20:
  print("저체중입니다")
elif bmi<=24:
  print("정상체중 입니다")
elif bmi<=29:
  print("과체중 입니다")
  
elif bmi>=30:
  print("과체중 입니다")
