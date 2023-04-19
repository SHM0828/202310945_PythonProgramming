for s in range (2,7,4):
    for i in range (1,10):
        for l in range (s,s+4):
            print(f'{l} x {i} = {i*l:2d}',end='\t')
        print()
    print()
