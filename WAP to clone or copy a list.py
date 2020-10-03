list1=[]
size=int(input('enter the size of the list\n'))
print('enter the elements of first list\n')
for i in range(size):
    i=int(input('enter the element'))
    list1.append(i)
print('first list is-',list1)
clonelist=list(list1)
print('copied list is',clonelist)
