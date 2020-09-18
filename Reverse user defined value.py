def reverse(num):
    rev_num=0
    r=0
    while(num>0):
        r=num%10
        rev_num=rev_num*10+r
        print("reminder", r)
        print("sum r", rev_num)
        num=num//10
        print('reverse of the number is',rev_num)
    
num=int(input('enter the number'))    
while(num<=0):
    print('enter the valid positive integer number')
    num=int(input('enter the number'))
print('reverse of the number',reverse(num))
