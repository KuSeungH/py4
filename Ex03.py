# ex03.py
# 리스트와 제어문을 활용하여 멤버 관리 프로그램 만들기


memberList = ['단비']

while True:

    print('1. 목록 ㅣ 2. 추가 ㅣ 3. 검색 ㅣ 4. 삭제 ㅣ 0. 종료')
    menu = int(input('원하는 메뉴를 입력하세요 >>> '))

    if menu == 1:
        print(memberList)

    elif menu == 2:
        newbie = input('추가할 멤버의 이름 입력 : ')
        memberList.append(newbie)

    elif menu == 3:
        search = input('검색할 멤버의 이름 입력 : ')
        flag = False
    for member in memberList:
        # if search == member:  # 검색어와 일치하는 결과 찾기
         if search in member:   # 검색어를 포함하는 결과 찾기
            flag = True
            print(member)
            break
    if flag == False:
        print('검색 결과를 찾을 수 없습니다')


    elif menu == 4:
        search = input('삭제할 멤버의 이름 입력 : ')
        
        if search in memberList:
            index = memberList.index(search)            # search가 위치한 index를 찾아서
            deleted = memberList.pop(search)            # remove는 반환이 없고
                                                       # pop은 삭제한 값을 반환한다
            print('{} : 삭제되었습니다'.format(search))
        else: 
            print('삭제할 데이터가 없습니다')

    # list.remove(object)           삭제할 요소를 지정
    # list.pop(index)               삭제할 요소의 index를 지정
    elif menu == 0:
        break
    
    print()
    

print('프로그램 종료!!')
