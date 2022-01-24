#이름: 점수 1. 추가 2. 점수 변경 3. 삭제 4. 학생목록리스트 출력 5. 1등 학생의 이름 출력 6. 종료
stu={}
while True :
    print()
    print('=== 학생부 프로그램 ===')
    print('1. 추가 2. 변경 3. 삭제 4. 출력 5. 1등 6.종료')
    act=int(input('입력 : '))
    if act==1 :
        name=input('학생 이름 : ')
        while True :
            score=int(input('학생 점수 : '))
            if 0<=score<=100 :
                break
            print(' 점수 오류 ')
        stu[name]=score
        print(name+' 학생 추가')
    elif act==2 :
        if len(stu)==0 :
            print(' 아직 저장된 학생이 없습니다 ')
        while True :
            name=input('변경할 학생 이름 : ')
            if name in stu: ## --> 딕션어리는 무조건 키만 비교함 값은 중복된 값이 있을수도 있기 때문에
                break
        while True :
            score=int(input('바꿀 점수 입력 : '))
            if 0<=score<=100 :
                break
        stu[name]=score
        print(name+'학생 점수 변경 ')
    elif act==3 :
        if len(stu)==0 :
            print(' 아직 저장된 학생이 없습니다 ')
            continue
        while True :
            name=input('삭제할 학생 이름 : ')
            if name in stu:
                break
        del stu[name]
        print(name+'학생 삭제 ')
    elif act==4 :
        if len(stu)==0:
            print(' 아직 저장된 학생이 없습니다 ')
            continue
        print('== 학생 목록 ==')
        mList=list(stu.keys())
        sList=list(stu.values())
        for i in range(len(stu)):
            print(str(i+1)+'. '+mList[i]+'학생 :: 점수 '+str(sList[i])+'점') ## sList 없이 stu[nList[i]]로 해도 가능
    elif act==5 :
        sList=list(stu.values())
        mList=list(stu.keys())
        big=sList[0]
        index=0
        for i in range(len(stu)):
            if big<=sList[i]:
                big=sList[i]
                index=i
        print('1등은 '+str(mList[index])+' 학생 , '+str(big)+'점')
    elif act==6 :
        print(' 종료 ')
        break
    else :
        print(' 입력 오류 ')
