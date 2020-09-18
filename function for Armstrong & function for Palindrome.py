num=int(input('enter a number'))
sum=0
temp=num
while temp>0:
        digit=temp%10
        sum+=digit**3
        temp//=10
if num==sum:
        print(num,"is an armstrong number")
else:
        print(num,"is not an armstrong number")


num1=int(input('enter a number'))
te=num1
rev=0
while(num1>0):
        dig=num1%10
        rev=rev*10+dig
        num1=num1//10
if(te==rev):
        print('the number is palindrome!')
else:
        print('not a palindrome!')
