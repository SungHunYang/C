'''
캐릭터 생성시 유저 이름 필요 
life =1 , maxhp=100 일반
life=2 , maxhp=100 사전예약
life=그대로 최대체력maxhp=100--> 200 현질러
현재 체력 attack(x) : hp-=x -> 0이하, life-=1
life=0 , attack 함수 수행 불가 게임 종료
show 호출시 캐릭터 이름과 현재 상화들 출력
'''

class Cha:
    def __init__(self, user,check=False):
        self.user=user  # __init__()여기 안에 들어있으면 굳이 선언 하지 않아도 자기자신한테 있다고 알아들
        self.__life=1
        if check:
            self.__life+=1
        self.maxhp=100
        self.hp=self.maxhp
        print('캐릭터 생성 되었습니다.')
    def cash(self):
        self.maxhp*=2
        self.hp=self.maxhp
        print('결제 완료 되었습니다!')
    def lifech(self):
        if self.__life==0:
            print('게임 오버..')
            return True
        return False
    def attack(self,x=30):
        if not self.lifech():
            self.hp-=x
            if self.hp<=0:
                self.__life-=1
                self.hp=100
                print('생명이 ''1'' 줄었습니다.')
                self.lifech
    def show(self):
        print(self.user,'님 캐릭터의 현재체력:',self.hp,', 생명:',self.__life)

c1=Cha('피즈',)
c1.attack(50)
c1.attack(50)
c1.attack(50)
c1.show()
ChaList=[Cha('유저'),Cha('아무무'),Cha('아리'),c1]
#-- > 이렇게 클래스를 리스트로 만들수 있다
for v in ChaList:
    v.show()
