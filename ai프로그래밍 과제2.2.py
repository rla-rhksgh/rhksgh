c=int(input('섭씨 온도를 입력하세요: '))
f=(9/5)*c + 32
print('섭씨 온도는 화씨',f, '도 입니다')




f=int(input('화씨 온도를 입력하세요: '))
c=(f-32)*5/9
print('화씨온도는 섭씨', c, '도 입니다')





radius=11
pi=3.141592
a=2*pi*radius
b=pi*radius**2
print('원의 반지름=', radius)
print('원의 둘레=', a)
print('원의 면적=', b)



radius=int(input('원의 반지름: '))
pi=3.141592
print('원의 반지름:', radius)
print('원의 둘레:', 2*pi*radius)
print('원의 면적:', pi*radius**2)




a=int(input('밑변을 입력하세요: '))
b=int(input('높이를 입력하세요:' ))

c=(a**2+b**2)**0.5
print('빗변:', c)


print(2<<0)
print(2<<1)
print(2<<2)
print(2<<3)
print(2<<4)
print(2<<5)
print(2<<6)
print(2<<7)
print(2<<8)
print(2<<9)


a=int(input('정수를 입력하세요'))
b=a>0 and a<100 and a%2==0
print('이 수가 짝수인가요?', b)

a=int(input('정수를 입력하세요'))
b=a>0 and a<100 and a%2==0
print('이 수가 짝수인가요?', b)



a=int(input('정수를 입력하세요'))
b=a>0 and a<100 and a%2==0
print('입력된 정수는 0에서 100의 범위 안에 있는 짝수인가요?', b)
a=int(input('정수를 입력하세요'))
b=a>0 and a<100 and a%2==0
print('입력된 정수는 0에서 100의 범위 안에 있는 짝수인가요?', b)


print(bin(5),'&',bin(6),'=',bin(5&6))
print(bin(5),'|',bin(6),'=',bin(5|6))
print(bin(5),'^',bin(6),'=',bin(5^6))



print(bin(6))


a=int(input('정수를 입력하시오'))
print(str(a)+'의 2진수 값:'+str(bin(a)))
print(str(a)+'의 2진수 값에 대한 비트단위 부정값:'+str(bin(-a)))



a=int(input('정수a를 입력하시오'))
b=int(input('정수b를 입력하시오'))
print('a/b의 몫', a//b)
print('a/b의 나머지', a%b)




a=int(input('세 자리 정수를 입력하세요'))
print('백의 자리:'+str(a//100))
print('십의 자리:'+str(a%100//10))
print('일의 자리:'+str(a%100%10))

a=int(input('세 자리 정수를 입력하세요'))
print('일의 자리:'+str(a%100%10))
print('십의 자리:'+str(a%100//10))
print('백의 자리:'+str(a//100))
















