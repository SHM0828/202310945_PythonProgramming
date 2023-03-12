#원주율 선택
def get_answer():
    global pi
    answer = input('선택: ')
    if answer == '1':
        pi = 3.14
        print('원주율을 ',pi,'로 설정했습니다.', sep='')
    elif answer == '2':
        pi = 'π'
        print('원주율을 ',pi,'로 설정했습니다.', sep='')
    else:
        print('1 또는 2 를 입력해주세요.')
    print()

#반지름 입력
def get_radius(prompt):
    r = int(input(prompt))
    return r
    
#원 넓이 구하기
def get_circle_area(radius):
    if pi == 3.14:
        circle_area = r ** 2 * pi
    else:
        circle_area = str(r ** 2) + pi
    print(str(r)+'x'+str(r)+'x'+str(pi)+'='+str(circle_area))
    return circle_area

#실행
print('반갑습니다! 반지름에 따른 원의 넓이를 계산해드리겠습니다.')

pi = 0
while pi == 0:
    print('원주율을 3.14로 하려면 1 을 입력, π로 하려면 2 를 입력해주세요.')
    get_answer()
    
r = get_radius('넓이를 구하려는 원의 반지름을 정수로 입력해주세요: ')
if r < 0:
    print('대신 입력해주신 ',r,'의 절대값을 반지름으로 가지는 원의 넓이를 계산해드리겠습니다.', sep='')
    r = r * -1
else:
    print('반지름이 ',r,'인 원의 넓이를 계산해드리겠습니다.', sep='')

circle_area = get_circle_area(r)
print('원의 넓이는 ',circle_area,'입니다.', sep='')
