
#if문 수 크기 비교 프로그램
a=int(input("입력"))
b=int(input("입력"))
c=int(input("입력"))
if a<b and a<c and b<c:
    print (a,b,c)
elif a<b and a<c and b>c:
    print(a,c,b)
elif b<a and b<c and c<a:
    print(b,c,a)
    
elif b<a and b<c and c>a:
    print(b,a,c)
elif c<a and c<b and b<a:
    print(c,b,a)
elif c<a and c<b and b>a:
    print(c,a,b)
