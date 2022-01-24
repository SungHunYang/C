#상속(ingeritance)
#부모클래스, 베이스클래스, 상위클래스 -> 보다 일반적인 개념(General)
#자식클래스, 파생클래스, 하위클래스 -> 보다 세부적인 개념
# 자식이 부모한테 포함된 관계 
# 코드 재사용성 증가 , 중복코드 최소화

class A:
    num=int()
    def a(self):
        print('A클래스의 메서드')

class B(A): # (A) 가 상속 관계 부여 
    def b(self):
        print('B클래스의 메서드')

