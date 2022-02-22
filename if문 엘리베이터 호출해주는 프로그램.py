#IF문 엘리베이터 호출해주는 프로그램
my = int(input("내 위치는?"))
a = int(input("A위치는?"))
b = int(input("B위치는?"))
if abs(a-my) == abs(b-my):
    if a>b:
        print("A 엘리베이터 호출하기")
    else:
        print("B 엘리베이터 호출하기")
else:
    if abs(a-my) < abs(b-my):
        print("A엘리베이터 호출하기")
    else:
        print("B엘리베이터 호출하기")
