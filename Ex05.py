# ex05.py
# dict 활용

member1 = {
    'name' : '짱구',
    'age' : 7,
    'from' : '짱구는 못말려'
}
member2 = {
    'name' : '흰둥이',
    'age' : 2,
    'from' : '짱구는 못말려'
}
member3 = {
    'name' : '단비',
    'age' : 5,
    'from' : '아따아따'
}
memberList  =[member1, member2, member3]

for member in memberList:
    text = '{}는 {}살이고, "{}" 에 출연합니다'
    text = text.format(member['name'], member['age'], member['from'])
    print(text)

print(memberList)
