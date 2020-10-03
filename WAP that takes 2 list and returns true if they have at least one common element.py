def check1(list1,list2):
    result=False
    for i in list1:
        for j in list2:
            if(i==j):
                result=True
                return result
                break
list1=[]
list2=[]
size=int(input('enter the size of the list\n'))
print('enter the elements of first list\n')
for i in range(size):
    i=int(input('enter the element '))
    list1.append(i)
print('first list is-',list1)
print('enter the elements of second list\n')
for i in range(size):
    i=int(input('enter the element'))
    list2.append(i)
print('second list is-',list2)
print(check1(list1,list2))
          
