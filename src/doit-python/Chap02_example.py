# 1번s
n1 = 14 % 4
print(n1)
# 2번
n2 = round(1.12345, 2)
print(n2)

# 3번
# a = input('나이를 입력하세요: ')
# n3 = 40 - int(a)
# print(n3)

# 4번
plus = lambda x, y : x + y
n4 = plus(34, 54)
print(n4)

# 5번
def mean(a, b):
    return ((a + b) / 2)
n5 = mean(33, 22)
n5 = 43 + n5
print(n5)

# 6번
b = [1, 2, 3, 10, 11, 12]

for i in b:
    if i< 10:
        print(i)
    else:
        print(i % 10)
