
import random # random 임폴트 해주기

print('어서오세요, 요거프레스입니다!')

##random.randrange(1,7) # 1~(7-1)까지
def cnn(cnt,start,end):
    if start<=cnt<=end:
        return True
    print('범위 확인후 다시 입력하세요')
    return False
def menu(num,start,end):
    if start<=num<=len(cafe):
        return True
    print('범위 확인후 다시 입력하세요')
    return False
def re():
    while True:
        num=input('재주문 하시겠습니까?')
        Ylist=['yes','YES','Yes','Y','y']
        Nlist=['no','NO','No','N','n']
        if num in Ylist:
            return True
        elif num in Nlist :
            return False
        else :
            continue
cafe={'아메리카노':1000, '카페라떼':3500,'프라프치노':5800}

while True :
    print('==메뉴 리스트==')
    mList=list(cafe.keys())
    pList=list(cafe.values())
    for i in range(len(cafe)) :
        print(str(i+1)+'. '+mList[i]+', '+str(pList[i])+'원')
    while True:
        num=int(input('메뉴번호 : '))
        if menu(num,1,len(cafe)):
            break
    while True :
        cnt=int(input('개수입력: '))
        if cnn(cnt,1,10):
            break
    print()
    pri=cnt
    print(mList[num-1],end=' ')
    pri*=cafe[mList[num-1]]
    print('를 '+str(cnt)+'개 주문하셨습니다.')
    print('총 가격은 '+str(pri)+'원입니다.')
    print('감사합니다!~')
    print()

    if re() :
        continue
    print('종료')
    break
         






