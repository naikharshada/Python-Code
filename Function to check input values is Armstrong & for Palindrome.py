def checkarm(num):
    rev_num=0
    r=0
    count=0
    my_num=num
    while(my_num>0):
        r=my_num%10
        count=count+1
        my_num=my_num//10
    r=0
    my_num=num
    while(my_num>0):
        r=my_num%10
        rev_num=rev_num+r**count
        my_num=my_num//10
    if(rev_num==num):
        print(num,' is an armstrong number')
    else:
        print(num,' is not an armstrong number')
        
def checkpalin(num):
     rev_num=0
     r=0
     my_num=num
     while(my_num>0):
         r=my_num%10
         rev_num=rev_num*10+r
         my_num=my_num//10
     if(rev_num==num):
         print(num,' is a palindrome number')
     else:
         print(num,' is not an palindrome number')

check='y'
while(check=='y'):
    num=int(input('enter the number'))
    while(num<=0):
        num=int(input('entered number is invalid enter any valid number'))
    check2=input('enter "a" if you want to check for armstrong else enter "p" if you want to check for palindrome')
    if(check2=='a'):
        checkarm(num)
    elif(check2=='p'):
        checkpalin(num)
    else:
        print('you did not entered the correct alphabet, enter "a" or "p" ')
    check=input('enter "y" if you want to check for more numbers else enter "n" ')
