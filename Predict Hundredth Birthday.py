from datetime import datetime
current_year=int(datetime.now().year)
name=input('enter your name')
age=int(input('enter yor age'))
print(name,'you will become 100 in',((current_year-age)+100))
