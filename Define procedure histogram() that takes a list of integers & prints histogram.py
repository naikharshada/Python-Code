def histogram(li):
    for i in li:
        temp=0
        while(temp<i):
            print('*',end='')
            temp+=1
        print('\n')

list1=[4,9,7]
histogram(list1)
