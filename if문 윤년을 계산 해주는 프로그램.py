
#if문 윤년을 계산 해주는 프로그램
a=int(input("년도 입력"))
if a%4==0 and a%100>0:
    print("윤년입니다")
elif a%400==0:
    print("윤년입니다")
else:
    print("윤년 이 아닙니다")
    

        
        
