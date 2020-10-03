import operator
dict1={1:12,3:14,4:13,2:11,0:10}
print('the original dictionary is:',dict1)
ascending=sorted(dict1.items(),key=operator.itemgetter(0))
print('dictionary in ascending order by value:',ascending)
descending=sorted(dict1.items(),key=operator.itemgetter(0),reverse=True)
print('dictionary in descending order by value:',descending)

