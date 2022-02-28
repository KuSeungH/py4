# exo2.py
# 리스트와 for문

list1 = [2, 7, 4, 8, 6, 'Hello', 'ITBANK']
# 리스트 : 서로 다른 자료형을 순서대로 묶어서 관리
# 리스트의 각 요소는 index라고 하는 순번에 의해서 관리
# 리스트의 index는 항상 0부터 시작한다

print(list1[0])
print(list1[1])
print(list1[2])
print(list1)

for i in range(7):                  # 7번 반복하여 list1의 i번째 요소를 출력
    print(list1[i])

for i in range(len(list1)):        # 리스트의 길이만큼 반복하여 list1의 i번쨰 요소 출력
    print(list1[i])

for element in list1:              # list1의 각 요소를 element라고 할 때
    print(element)                 # element를  출력 (순번이 사용되지 않음)

from os import remove, system
system('cls')

list2 = ['짱구', '유리', '철수', '훈이', '맹구']
print(list2)

list2.sort()
print(list2)

list2.sort(reverse=True)
print(list2)

list2.append('짱아')
print(list2)

list2.remove('철수')
print(list2)

list2.insert(2, '흰둥이')
print(list2)