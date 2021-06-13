import re

# 1
words = ['apple', 'cat', 'brave', 'drama', 'arise', 'blow', 'coat', 'above']

for i in words:
    m = re.match(r'a\D+', i)
    if m :
        print(m.group())


# 2
a = '제 이메일 주소는 greatking@naver.com입니다. 오늘 저는 travel.daum.net 라는 주소로 메일을 보내려고 합니다. 저는 apple@gmail.com, life@abc.co.kr 라는 메일도 사용하고 있습니다.'
b = re.findall(r'[a-z]+@[a-z.]+', a)
print(b)

# 3
exam = '저는 92년에 태어났습니다. 88년에는 올림픽이 있었습니다. 지금은 2020년입니다.'
c = re.findall('\d.+?년', exam)
print(c)

# 4
d = 'I have a dog, I am not a girl. You ar not alone. I am happy'
d2 = re.split('\.', d)
print(d2)

#5
e = "Chandler: All right Joey, be nice. So does he have a hump? A hump and a hair-piece Phoebe: Wait, does he eat chalk? Pheobe: Just, because, I don't want her to go through what I went through with Carl- oh!"
m = re.findall('[A-Za-z]+:', e)
print(m)
M = list(set(m)) #중복 제거 
print(M)