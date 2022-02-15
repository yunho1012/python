#for문 100까지 369 하는 프로그램

e=0
s=0

for x in range(1,101,1):
    e=x%10
    s=x//10
    if s == 3 or s==6 or s==9:
        if e==3 or e==6 or e==9:
            print("짝짝")
        else:
            print("짝")
    elif e==3 or e==6 or e==9:
        print("짝")

    else:
        print(x)
    
