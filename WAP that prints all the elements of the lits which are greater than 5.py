a=[]
size=int(input('enter the size of the list'))
count=1
while(count<=size):
    item=int(input('enter element of list'))
    a.append(item)
    count+=1
print('the to be checkedis=',a)
a2=[]
for i in a:
    if(i<5):
        a2.append(i)
print('this list contain all elements of the previous one which are less than 5',a2)
