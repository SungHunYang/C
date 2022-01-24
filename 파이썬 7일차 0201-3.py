class A:
    __abc='apple'
    # __(언더바 2개) 하면 클래스 밖에서는 건들수 없다 (JAVA 에서 private랑 비슷)
    # 이름 장식(Name Mangling)
    # 의도하지 않은 접근을 방지 하고자 하는 목적으로 사용 
    def show(self):
        print('abc는 '+self.__abc+'입니다') #--> 그냥 self.abc 하면 안나옴 self.__abc 해야됨
    # 이름 장식된 멤버는 본인 클래스 내부에서 접근 가능
    # 이름 장식된 멤버에 접근가능하도록 하는 함수(메서드)
    # getter, setter
    def get_abc(self): # 멤버값을 받아서 리턴해주는 함수
        return self.__abc
    def set_abc(self,abc): # 멤버의 값을 설정(대입,저장) 해주는 함수
        self.__abc=abc

a=A()
# a.abc='banana' --> 이건 불가능
a.show()
print(a.get_abc)
