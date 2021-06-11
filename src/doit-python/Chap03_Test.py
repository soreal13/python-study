import os, re, codecs

# 현재 위치 확인
print(os.getcwd())

# 폴더 이동하기
# os.chdir()

# 폴더 안 파일 확인
print(os.listdir())

folderFile = os.listdir()
print(type(folderFile)) # list
print(folderFile)

# 파일 입출력
# f = open('a.txt', 'w') # w 쓰기 모드
# f.write('나는 파이썬 코딩 연습 중이다.')
# f.read()
# f.seek(0) # 파일 가장 처음으로 커서 이동하라는 의미
# f.close()

# 파일 문장추가
# f = open('a.txt', 'a') # a 추가 모드
# f.write('잘 하고 싶다.')
# f.close()
# f = open('a.txt', 'r')
# f.read()
# f.close()

# with 문
# with open('test.txt', 'w') as f:
#     f.write('읽기 모드로 열고 쓴다.') # f.close()로 파일 객체 닫을 필요 없음.

# 한글 인코딩 문제
# f = codecs.open('한글파일.txt', 'r', 'utf-8')
# f.read()[:10]

# 정규표현식
example = '이동민 교수님은 다음과 같이 설명했습니다(이동민, 2019). 그런데 다른 교수님은 이 문제에 대해서 다른 견해를 가지고 있었습니다.(최재영, 2019). 또 다른 견해도 있었습니다(Lion, 2018)'
result = re.findall(r'\([A-Za-z가-힣]+, \d+\)', example)
print(result)

# match 메서드
pattern = r'life'
script = 'life'
re.match(pattern, script)
re.match(pattern, script).group() # life, group() 함수는 반환

re.match(r'life', 'life').group() # 문자열 life에서 life라는 패턴 찾아 반환하라

def refinder(pattern, script):
    if re.match(pattern, script):
        print('Match!')
    else:
        pritn('Not a match!')

refinder(r'Life', 'Life is so cool')

# search 문자열 전체에서 패턴찾기
re.search(pattern, script).group

# findall 패턴 모두 찾아 리스트로 반환
number = 'My number is 511223-1***** and yours is 521012-2*****'
re.findall('\d{6}', number) # '\d{6}' 패턴은 숫자를 여섯 번 반복한 값을 의미한다.

# 탐욕(greedy) 검색
result = re.findall(r'\(.+\)', example)
print(result) # .+ 명령어를 탐욕스럽게 인식함
# ['(이동민, 2019). 그런데 다른 교수님은 이 문제에 대해서 다른 견해를 가지고 있었습니다.(최재영, 2019). 또 다른 견해도 있었습니다(Lion, 2018)']

result = re.findall(r'\(.+?\)', example)
print(result) # ?를 달아주면 제대로 검색이 됨. 
# ['(이동민, 2019)', '(최재영, 2019)', '(Lion, 2018)']\

# split() 문장 나누는 패턴 만들기
data = 'a:3; b:4; c:5'
for i in re.split(r';', data):
    print(re.split(r':', i))

# ['a', '3']
# [' b', '4']
# [' c', '5']

# sub 메서드 - 문자열 바꾸기
sentence = 'I love a lovely dog, really. I am not telling a lie. What a pretty dog! I love this dog.'
re.sub(r'dog', 'cat', sentence) # I love a lovely cat, really. I am not telling a lie. What a pretty cat! I love this cat.

words = 'I am home now. \n\n\nI am with my cat \n\n'
re.sub(r'\n', '', words)

print(re.findall(r'\w+ly', sentence))