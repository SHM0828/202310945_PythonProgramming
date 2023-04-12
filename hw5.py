def read_single_digit(in1):
    if in1=='1': return '일'
    elif in1=='2': return '이'
    elif in1=='3': return '삼'
    elif in1=='4': return '사'
    elif in1=='5': return '오'
    elif in1=='6': return '육'
    elif in1=='7': return '칠'
    elif in1=='8': return '팔'
    elif in1=='9': return '구'
    else: return '영'
    
def read_number(in1):
    return f'{read_single_digit(in1[0])}{read_single_digit(in1[1])}{read_single_digit(in1[2])}'
    
print(read_number(str(int(input('세자리 정수 입력: ')))))
