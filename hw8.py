def buy(in1):
    print('[구입]')
    item = input('상품 이름: ')
    if item=='': return False
    try:in1[item] = int(input('수량: '))
    except:print('수량을 정수로 입력해주세요.');buy(in1)
    print()
    
def show(in1):
    print(f'\n장바구니: {in1}')
    
def find(in1):
    finding=input('\n확인하고자 하는 상품의 이름: ')
    if finding in in1: print(f'{finding}(은)는 {in1[finding]}개 담겨 있습니다.')
    else: print(f'장바구니에 {finding}은(는) 없습니다.')

shopping_bag = {}
while True:
    if buy(shopping_bag) == False:
        break
show(shopping_bag)
find(shopping_bag)
