
#if문 40분전 시간을 알려주는 프로그램
a,b=input("입력").split(':')
a = int(a)
b = int(b)
if b>40:
    print( a, ":",b-40)
elif b<40:
    if a == 0:
        a = 23
        print(a, ":",60+b-40)

    else:
        print(a-1, ":",60+b-40)
elif b==40:
    print( a, ":",00)
