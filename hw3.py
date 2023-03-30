def get_fixed_price(in1):
    out1 = in1 * (100 / (100 - dc))
    return out1

dc = float(input('할인율을 입력해주세요: '))
price1 = int(input('A상품의 할인된 가격을 입력해주세요: '))
price2 = int(input('B상품의 할인된 가격을 입력해주세요: '))
print('A상품의 정가: ',get_fixed_price(price1))
print('B상품의 정가: ',get_fixed_price(price2))
