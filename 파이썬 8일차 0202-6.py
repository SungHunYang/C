class Ani:
    def speak(self):
        print('울음소리')
    def act(self):
        print('액션 소개')

class Dog(Ani):
    def speak(self):
        print('멍멍')
    def ball(self):
        print('공놀이')
    def act(self):
        print('1.울음 소리 듣기')
        print('2. 공놀이')
        a=int(input('입력 : '))

class Cat(Ani):
    def speak(self):
        print('야옹')
    def sleep(self):
        print('zzZ..')
    def act(self):
        print('1.울음 소리 듣기')
        print('2. 잠자기')
        a=int(input('입력 : '))

# 1. 여러 객체들을 하나의 리스트에 저장했을때
# 2. 어떤 객체가 어떤 클래스에 해당하는지 찾아낼 함수가 필요
# 3. 어떤 메소드를 수행할수있는지 확인 
'''
d=Dog()
c=Cat()
xList=[d,c]
'''
def checkClass(c):
    if type(c) is Dog:
        print('Dog클래스 입니다.')
        return 1
    elif type(c) is Cat:
        print('Cat클래스 입니다.')
        return2
            
def f1():
    print('1.울음 소리 듣기')
    print('2. 공놀이')
    act=int(input('입력 : '))
    if act==1:
        v.speak()




xList=[Dog(),Cat()]
for v in xList :
    v.speak()

for v in xList:
    a=checkClass(v)
    v.act()









