
#while문 0을 입력할 떄까지 무한히 입력받다가 0을 입력 받으면 총합을 알려주는 프로그램
a=0
b=0

while True:
    a=int(input("입력"))
    b=b+a
    if a==0:
        break
print(b)

