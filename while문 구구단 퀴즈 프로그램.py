
#while문 구구단 퀴즈 프로그램
import random
import time


endtime = time.time() + 10
d=0

while time.time() <= endtime:
    a=random.randint(1,9)
    b=random.randint(1,9)
    print(a,"x",b,"=")
    c=int(input("정답은?"))
    if c==a*b:
        print("정답")
        d+=1

    else:
        print("오답")

print("10초동안",d,"개 맞췄습니다")
