shopping_bag = {}
print('[구입]')
while True:
    item = input('상품 이름: ')
    if item=='':break
    else:count = int(input('수량: '));shopping_bag[item]=count;print(f'장바구니에 {item}(이)가 {count}개 담겼습니다.\n')
print(f'\n장바구니: {shopping_bag}')

print('\n[검색]')
finding=input('확인하고자 하는 상품의 이름: ')
print(f'{finding}(은)는 {shopping_bag[finding]}개 담겨 있습니다.')
