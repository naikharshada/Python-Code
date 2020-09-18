def fibbo(limit):
    print('The fibonaci series till limit "limit" is:')
    a0=0
    a1=1
    print(a0,a1,end='')
    for i in range (limit-2):
        a2=a1+a0
        print(a2,end= ' ')
        a0,a1=a1,a2
        
limit=int(input('enter the limit'))
while(limit<=0):
    print('enter the valid limite that should be any positive integer')
limit=int(input('enter the limit'))
fibbo(limit)
