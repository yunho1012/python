#if문 일교차 계산 프로그램
a = int(input("아침 최저 기온을 입력해 주세요"))
b = int(input("오후 최고 기온을 입력해 주세요"))
c = b-a
if c<10:
  print("초여름 날씨 입니다")
elif c == 10:
  print("감기 조심 하세요")
else:
  print("감기 조심 하세요")


