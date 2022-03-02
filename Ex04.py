# ex04.py
# dictionary
from this import d


li1 = []
print(type(li1))

dict1 = {}
print(type(dict1))

'''
    리스트가 여러 요소를 index를 활용하여 구분하고 관리한다면
    dict는 index 대신 임의의 key값을 이용하는 value를 관리한다

    key : value 를 1:1 맴핑하여 사전처럼 저장하기 때문에 dict라고 한다
    (자바에서는 map이라고 부른다. mapping 하여 저장하는 형태)

    [dict]                 [list]
    apple : 사과            0 : 사과
    banana : 바나나         1 : 바나나
    car : 자동차            2 : 자동차
    3456 : 100만원

    key와 value가 1:1로 맴핑되긴 하지만
    key를 알면 value를 구할 수 있고,
    value를 안다고 해서 역으로 맵핑된 key를 추적할 수는 없다
    즉, key와 value의 연결은 양방향이 아니다

    key의 이름은 중복을 허용하지 않는다
    (리스트의 index는 1씩 증가하므로 절대 중복되지 않는다)
    (마치 변수의 이름과 같다)


    value는 중복을 허용하다
    (서로 다른 key로 접근해서 같은 value가 나올 수 있다)
'''

dict1 = {
    'apple' : '사과',
    'banan' : '바나나',
    'car' : '자동차',
    'dice' : '주사위',
}

print(dict1)
print(dict1['apple'])
print(dict1.get('banana'))

print(dict1.keys())
print(dict1.values())

dict1['elephant'] = '코끼리'        # dict에 값 추가
dict1['carpet'] = '카페트'
del dict1['car']                  # dict에 값 삭제

for key in dict1.keys():
    value = dict1.get(key)
    # print('key :', key, ', value :', value)
    print('{}의 뜻은 {} 입니다'.format(key, value))

