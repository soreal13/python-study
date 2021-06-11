#19단 곱셈
# for item in range(2, 20):
#     for each in range(2, 20):
#         print(item, ' X ', each, ' = ', item*each)

#print 예제
# print('나는 사과 %d개를 먹었습니다.' %2)
# print('나는 사과 %d개와 배 %d개를 먹었습니다' %(2,3))


# 람다식
# y = lambda x :3 * x
# print(y(12))

# add = lambda a, b : a + b
# print(add(2,3))

# littlePrince = '''여섯 살 적에 나는 '체험한 이야기'라는 제목의 원시림에 관한 책에서 기막힌 그림 하나를 본적이 있다. 맹수를 집어삼키고 있는 보아뱀 그림이었다. 위의 그림을 그것을 옮겨 그린 것이다. 그 책에는 이렇게 씌여 있었다.
# '보아뱀은 먹이를 씹지도 않고 통째로 집어삼킨다. 그리고는 꼼짝도 하지 못하고 여섯 달 동안 잠을 자면서 그것을 소화시킨다.' '''

# print(littlePrince[:10])

#10줄까지 출력하는 함수
# short = lambda x : x[:10]
# print(short(littlePrince))

#계산기
# def calculator(a, b):
#     return a + b, a - b, a* b, a / b
# print(type(calculator)) #function 
# print(type(calculator(2, 3))) #tuple

# def separate():
#     a = int(input('자연수 중 하나를 입력하세요: '))
#     if a % 2 == 0:
#         print('짝수입니다.')
#     else:
#         print('홀수입니다.')

# separate()

#서비스 가격 출력 프로그램
price = [23, 40, 67]

for i in price:
    i * 1.1

def service_price():
    service = input('서비스의 종류를 입력하세요, a/b/c: ')
    valueAdded = input('부가세를 포함합니까? y/n: ')
    if valueAdded == 'y': # 부가세 존재
        if service == 'a':
            result = price[0] * 1.1
        elif service == 'b':
            result = price[1] * 1.1
        elif service == 'c':
           result = price[2] * 1.1
    else: #부가세 없을때
        if service == 'a' :
            result = price[0]
        elif service == 'b':
            result = price[1]
        elif service == 'c':
            result = price[2]
    print(round(result, 1), '만 원입니다.')
    
service_price()



