import time # 시간 멈추기 임폴트

mList=['아메리카노','카페라떼','프라프치노']
pList=[1000,3500,5800]

print('==== 메뉴 관리 프로그램 ====')
while True :
    print()
    print('1. 추가 2. 메뉴변경 3. 가격변경 4. 삭제 5. 출력 6. 종료')
    act=int(input('입력 : '))
    if act==1:
        plus=input('원하는 메뉴 : ')
        more=int(input(' 가격 : '))
        mList.append(plus)
        pList.append(more)
    elif act==2:
        while True :
            plus=int(input('변경 메뉴 번호 : '))
            if 1<=plus<=len(mList):
                break
        mList[plus-1]=input('변경할 메뉴 : ')
    elif act==3:
        while True :
            plus=int(input('변경 가격 번호 : '))
            if 1<=plus<=len(mList):
                break
        mList[plus-1]=int(input('변경할 가격 : '))
    elif act==4:
        plus=int(input('삭제할 메뉴 번호 : '))
        mList.remove(mList[plus-1])
        pList.remove(pList[plus-1])
    elif act==5:
        print('=== 메뉴 리스트 ===')
        for i in range(len(mList)):
            print(str(i+1)+'. '+mList[i]+', '+str(pList[i])+'원')
    elif act==6:
        print('프로그램 종료')
        break
    else :
        print('번호 재입력')

    if 1<= act<=4:
        for i in range(2):  # .. 이 1초 쉬면서 2번 돈다는 뜻
            print('..', end=' ') 
            time.sleep(1) # 1초 잠시 시간을 멈춘다.
        print('처리 완료')
