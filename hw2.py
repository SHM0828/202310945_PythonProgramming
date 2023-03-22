def get_integer(in1):
    out = int(input(in1))
    return out
    
def exchange(in1):
    q500 = in1 // 500
    r500 = in1 % 500
    q100 = r500 // 100
    r100 = r500 % 100
    q50 = r100 // 50
    r50 = r100 % 50
    q10 = r50 // 10
    r10 = r50 % 10
    print('500원 ',q500,'개,',sep='')
    print('100원 ',q100,'개,',sep='')
    print('50원 ',q50,'개,',sep='')
    print('10원 ',q10,'개',sep='',end='')
    if r10 != 0:
        print(',\n1원 ',r10,'개',sep='',end='')
    print('로 교환되었습니다.')

money = get_integer('동전으로 교환할 금액을 입력해주세요: ')
exchange(money)
