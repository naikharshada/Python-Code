def checkvow(str1):
    if(str1=='a' or str1=='e' or str1=='i' or str1=='o' or str1=='u' or str1=='A'
       or str1=='E' or str1=='I' or str1=='O' or str1=='U'):
        print('vowel')
    else:
        print('consonant')

str1=input('enter the strings of one character')
while(len(str1)<0):
     str1=input('enter the string of one character')
while(len(str1)>=2):
    str1=input('enter the string of one character')
    
checkvow(str1)
