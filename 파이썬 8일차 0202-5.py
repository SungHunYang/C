class A :
    def f1(self):
        print('안녕하세요!')
    def f2(self):
        print('A클래스')

class B(A):
    def f2(self):
        print('B클래스')
class C(A):
    def f2(self):
        print('C클래스')
class D(A):
    def f2(self):
        print('D클래스')
# [오버라이딩]
# 부모클래스의 메서드를 이용하고 싶지만
# 기능이 자식클래스의 입맛에 맞지 않을때
# 재정의 _ 오버라이딩 가능

