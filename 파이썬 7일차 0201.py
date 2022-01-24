# 객체지향코딩

#함수(메서드)에게 "주체, 주어"가 있는가?

#기본 단위 == 클래스
#클래스 ---객체화(인스턴스화):생성자 담당--> 객체를 생성
#생성자 라는 함수를 통해서 클래스 -> 객체
# 클래스 : 객체 = 1:N


class C:
    i=10 # 멤버변수, 속성, 필드
    s=int() # 타입만 지정하는것도 가능
    def show(self): #멤버함수, 메서드
        # 자기자신객체==self를 넣어서 객체가 호출할때 자기 자신을 인자로 넘기는 것을 허용한다.
        print('안녕하세요',self.i)

# 생성자 (함수_초기화함수) 중에서 인자가 없는 생성자를 디폴트 생성자, 기본생성자 라고 한다.
# . <- 멤버접근연산자
# 객체들 끼리는 멤버의 값을 공유하지 않는다.
# 만일 self 가 없을시 C.show() 를 하면 그냥 보여주기는 함 객체가 만들어 진건 x
c=C()   
c.i=1
c.show() # 객체가 멤버함수를 호출하게 되면 자기 자신을 인자로 넘긴다.


class Car:
    __speed=int() # 반드시 초기화 해줘야함, 초기화를 '0'대신 int()라고 하기도 함
    __maxSpeed=100
    def set_maxSpeed(self):
        self.__maxSpeed=int(input('변경할 최대속력 입력: '))
    def speedUp(self,x=50): # self는 반드시 넣어줘야함
       self.__speed+=x
       if self.__speed>=self.__maxSpeed:
           self.__speed=self.__maxSpeed
           print('위험 감속해주세요!')
    def speedDown(self,x=60):
        self.__speed-=x
        if self.__speed<=0:
            self.__speed=0
            print('속도가 0입니다.')
c1=Car()
c1.speedUp(100)


# 생성자(함수)를 통해 초기화를 해볼수있다.
class A:
    a=int()
    b=int()
    def __init__(self,a,b): # __init__() 초기화함수(생성자)
        # [재정의] --> 오버라이딩
        self.a=a
        self.b=b
    def show(self):
        print('a=',self.a,'b=',self.b)
a=A(10,20)
a.show()

#예제 책제목, 작가 알고있어야만 함 
class Book:
    name=str()
    author='' #--> 이렇게 해도됨 
    def __init__(self,name,author='작자미상'): # 이걸 사용하면 위에 name author명시하지 않아도 됨
        self.name=name
        self.author=author
        print('생성자로 객체생성완료')
    def read(self):
        print(self.name,'_',self.author,'을(를) 읽습니다...')

book1=Book('해리포터','JK롤링')
book1.read()








    














