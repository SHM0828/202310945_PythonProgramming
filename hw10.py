def input_scores():
    print('[점수 입력]')
    i=1
    while True:
        scoreAppend=int(input(f'#{i}? '))
        if scoreAppend<0:break
        else:score.append(scoreAppend)
        i+=1
    return score
        
def get_average(in1):
    sum=0
    for i in range(len(in1)):
        sum+=in1[i]
    return sum
    
def show_scores(in1):
    print('\n[점수 출력]\n개인점수: ',end='')
    for i in range(len(in1)):
        print(in1[i],end=' ')
    print(f'\n평균: {(sum/len(in1)):.1f}')

import os,pickle
score=[]
if os.path.exists('score.bin'):
    print('[파일읽기]')
    file=open('score.bin','rb')
    byte=pickle.load(file)
    while True:
        score.append(byte)
        try:byte=pickle.load(file)
        except:break
else:
    score=input_scores()
    file=open('score.bin','xb')
    for i in range(len(score)):
        pickle.dump(score[i],file)
file.close()

sum=get_average(score)   
show_scores(score)
