# ex01.py
# 중첩된 반복문 (이중 for문)

for i in range(2, 6):           # 1단에서  5단까지
    for j in range(1, 10):      # 1부터 9까지
        print('{} x {} = {}'.format(i, j, i * j))
    print()
print()

for j in range(1, 10):      # 1부터 9까지
    print('{} x {} = {}'.format(6, j, 6 * j))
print()


for i in range(5):
    for j in range(5):
        print('{:2d}'.format(i * 5 + j + 1), end=' ')
        # i와 j를 이용하여 1부터 25까지 숫자를 출력
    print()
print()

# 2중 for문으로 가로세로 개념을 만들어서 처리할 수도 있다

for i in range(5):
    for j in range(5):
        if (i + j) % 2 == 0:
            print('🐯', end='')
        else:
            print('🐻', end=' ')
    print()
print()

for i in range(5):
    for j in range(5):
        if i == 0 or i == 4 or j == 0 or j == 4:
            print('🐯', end='')
        else:
            print(' ', end=' ')
    print()
print()


for i in range(5):
    for j in range(5):
        print('[{}, {}]'.format(i, j), end=' ')