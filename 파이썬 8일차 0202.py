class Card:
    def __init__(self,user,money=5000,pw=1234):
        self.user=user
        self.money=money
        self.pw=pw
        print(self.user+'님, 카드 생성')
    def pay(self,money):
        if self.money<money:
            print('잔액 부족')
            return
        self.money-=money
        print('결제 완료')
    def outMoney(self):
        if self.checkPw():
            return
        money=int(input('출금 금액 입력 : '))
        if self.money<money:
            print('잔액 부족')
            return
        self.money-=money
        print('출금 완료')
    def checkPw(self):
        pw=int(input(self.user+'님, 비밀번호 입력 : '))
        if pw==self.pw :  # 배열이 아닐때 같은지 확인하는 방법에 ''is'' 가 있다 "12 is a" 같이
            return False
        print('비밀 번호 불일치 ')
        return True
    def changePw(self):
        if self.checkPw():
            return
        self.pw=int(input(self.user+'님, 새 비밀번호 입력 : '))
        print('비밀번호 변경 완료')

class Bus(Card) :
    def __init__(self,user,money=5000,pw=1234,age=20):
        self.user=user
        self.money=money
        self.pw=pw
        self.age=age
        print(self.user+'님, 카드 생성')
    age=int()
    def fare(self):
        if 8<self.age<20:
            print('학생입니다')
            Card.pay(self,1000)
        elif 20<=self.age<65:
            print('성인입니다')
            Card.pay(self,2000)
        else:
            print('승차합니다')
            print('결제완료')

class Credit(Card):
    def __init__(self,user,money=5000,pw=1234,limit=10000):
        self.user=user
        self.money=money
        self.use=0
        self.pw=pw
        self.limit=limit
        print(self.user+'님, 카드 생성')
    def pay(self): # 오버라이딩 재정의
        while True:
            x=int(input('원하는 금액 입력 ; '))
            self.use+=x
            if self.use>self.limit :
                print('한도 초과')
                break
            print('결제 완료')
            print('계속 결제 하시겠습니까?')
            a=int(input('1.계속 2.종료 :'))
            if a==2 :
                break
        

a=Bus('피즈')
a.fare()















    
    
