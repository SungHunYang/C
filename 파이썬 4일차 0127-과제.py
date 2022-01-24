'''
미어캣 키가 다들 재각각 입력 같은 값 입력 x
미어캣5마리가 줄서서 망을 보는데 오른쪽을 바라 보고 있다
미어캣 들이 자기 앞에 있는 키가 자기 보다 더큰 미어캣을 만나면 그 뒤를 볼수 없다
전체 볼수 있는 마리 수를 구해라
한명씩 전부 몇 마리 보이는지 
'''

mi=[]
for i in range(5) :
    while True :
        num=int(input('미어캣 사이즈 입력 : '))
        if num not in mi :
            break
    mi.append(num)
ki=[]

for i in range(5):
    num=0
    for a in range(1,5-i):
        if mi[i]<mi[i+a] :
            num+=1
            break
        num+=1
    ki.append(num)
print(mi)
print(ki)
hap=0
for v in ki :
    hap+=v
print('총합은',hap)           
