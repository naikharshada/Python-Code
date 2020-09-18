def func(num):
    if(num%2==0):
        print(num,'is even')
    else:
        print(num,'is odd')

check = 'y'
while(check=='y'):
    num=int(input('enter the number'))
    while(num<=0):
        print('enter the valid integer number')
    func(num)
    check=input('if you want to check more values then Press "y" or press any key to Exit ')
