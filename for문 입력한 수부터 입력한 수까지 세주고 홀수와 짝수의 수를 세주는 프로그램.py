#for문 입력한 수부터 입력한 수까지 세주고 홀수와 짝수의 수를 세주는 프로그램
a = int(input("숫자를 입력해주세요"))
b=0
c=0
for x in range(1,a+1):
    
    print(x,end='')
    if x%2==0:
        
        b+=1
    else:
        c+=1
print("홀수 개수는",c,"개")
print("짝수 개수는",b,"개")
