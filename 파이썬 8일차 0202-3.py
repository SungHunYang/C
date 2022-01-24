class Person:
    name=str()
    def __init__(self.name):
        self.name=name
    def hello(self):
        print('안녕하세요! 저는 '+self.name+'입니다')

class Stu(Person):
    score=int()
    def __init__(self,name):
        self.name=name
        #Person.__init__(self,name) _-> 이렇게 쓸수는 있다 self.name=name 과 똑같은 역할
        while True:
            self.score=int(input(self.name+'학생의 성적을 입력 하세요 :'))
            if 0<=self.score<=100:
                break
    def grade(self):
        if 0<=self.score<=60:
            print(self.name+'학생의 등급은 C 입니다')
        elif 61<=self.score<=80:
            print(self.name+'학생의 등급은 B 입니다')
        elif 81<=self.score<=100:
            print(self.name+'학생의 등급은 A 입니다')
            
a=Stu('진숙')

a.grade()
