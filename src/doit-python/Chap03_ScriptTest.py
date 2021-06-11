import os, re, codecs

f = codecs.open(r'gg1e01.txt', 'r', encoding = 'utf-8')
script101 = f.read()

# 특정 등장인물 대사만 모으기
Line = re.findall(r'DEAN:.+', script101)
print(Line[:3])

for item in Line[:3]:
    print(item)

f.close()

# 리스트로 대사 텍스트 파일에 저장
f = open('dean.txt', 'w', encoding='utf-8')

dean = ''

for i in Line:
    dean += i + '\n'

f.write(dean)
f.close()