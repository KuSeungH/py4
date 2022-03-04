# ex06.py
# list와 dilct를 조합한 전화번호부 만들기

from os import system


phoneBookList = []

while True:
    print('1. 목록')
    print('2. 검색')
    print('3. 추가')
    print('4. 삭제')
    print('0. 종료')
    menu = input('선택 >>> ')
    form = '{} : {}'

    if menu == '1':
        for pd in phoneBookList:
            print(form.format(pd['name'], pd['pnum']))
        print()

    elif menu == '2':
        search = input('검색할 사람의 이름 입력 : ')
        for pd in phoneBookList: 
            if pd['name'] == search:
                print(form.format(pd['name'], pd['pnum']))
            
    elif menu == '3':
        name = input('추가할 사람의 이름 입력 : ')
        pnum = input('{}의 전화번호 : '.format(name))
        pd = {
            'name' : name,
            'pnum' : pnum,
        }
        phoneBookList.append(pd)
    elif menu == '4':
        search = input('삭제할 사람의 이름 입력 : ')
        for i in range(len(phoneBookList)):
            pd = phoneBookList[i]
            if pd ['name'] == search:
                print(i)
                phoneBookList.pop(i)
                break # for문 탈출
    

    elif menu == '0':
        break
    else:
        print('메뉴를 다시 확인하고 입력해주세요')

    system('pause')
    system('clear')

    # system()

'''
    삭제를 구현해야 할때
    pop과 remove 중 어떤 것을 사용할 것인가?
    pop은 index(정수)가 필요하고
    remove는 객체가 필요하다
    간단하게 순번으로 삭제하려면 pop이 편하다

    index를 참조하기 위해서는 리스트의 멤버를 바로 참조하지 말고
     for i in range(len(list)) 의 형식으로 접근하자

    index를 알면 멤버를 찾아낼 수 있고, 삭제도 편리하게 할 수 있다

    단순히 목록만 출력하기 위해서라면 for item in list 형식으로 사용해도 된다
'''