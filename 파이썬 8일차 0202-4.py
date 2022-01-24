##카드 클래스
##사용자,비밀번호,잔액
##pay()
##inMoney()
##outMoney()
##changePW()
##checkPW()
class Card:
    def __init__(self,user,pw=1111,money=0):
        self.user=user
        self.pw=pw
        self.money=money
        print(self.user+'님, 카드생성완료!')
    def pay(self,money):
        if self.money<money:
            print('잔액부족!')
            return
        self.money-=money
        print('결제완료!')
    def outMoney(self):
        if self.checkPW():
            return
        money=int(input('출금금액입력: '))
        if self.money<money:
            print('잔액부족!')
            return
        self.money-=money
        print('출금완료!')
    def checkPW(self):
        pw=int(input(self.user+'님, 비밀번호입력: '))
        if pw==self.pw:
            return False
        print('비밀번호 불일치!')
        return True
    def changePW(self):
        if self.checkPW():
            return
        self.pw=int(input(self.user+'님, 새 비밀번호입력: '))
        print('비밀번호 변경완료!')

class Bus(Card):
    def __init__(self,user,pw=1111,money=5000,age=20):
        Card.__init__(self,user,pw,money)
        self.age=age
    def fare(self):
        if 8<self.age<20:
            m=1000
        elif 20<=self.age<65:
            m=2000
            Card.pay(self,2000)
        else:
            m=0

class Limit(Card):
    def __init__(self,user,pw=1111,money=5000,limit=10000):
        Card.__init__(self,user,pw,money)
        self.use=0
        self.limit=limit
    def pay2(self,money):
        if self.use+money>self.limit:
            print('한도초과!')
            return
        self.use+=money
        print('결제완료!')

b=Bus('피즈')
b.fare()



        
