list1=[]
size=int(input('enter the size of the list \n'))
while(size<6):
    print('enter the limit size greater than 5')
    size=int(input('enter the size of the list \n'))
for i in range(size):
    i=int(input('enter the element'))
    list1.append(i)
print('first list is-',list1)
print('after removing 0th,2nd,4th and 5th element from the list')
list1=[x for (i,x) in enumerate(list1) if i not in(0,2,4,5)]
print(list1)
