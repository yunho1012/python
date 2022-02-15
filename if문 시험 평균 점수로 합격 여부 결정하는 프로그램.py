#if문 시험 평균 점수로 합격 여부 결정하는 프로그램
a=int(input("수학점수 입력해 "))
b=int(input("국어점수 입력해 "))
c=int(input("과학점수 입력해 "))
d=a+b+c
e=d/3
print("총합:",d)
print("평균:",e)
if e<60:
    
    print("불합격임")
if e>=60:
    print("합격임")

