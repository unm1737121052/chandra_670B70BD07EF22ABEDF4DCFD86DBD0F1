# leap year

""
4==0
100!=0
400==0

""
def isleapyear(year):
  if(year%4==0 and year%100!=0)or year%400==0:
     return True
  else:
    return False

year=int(input("enter a year:"))
if isleapyear(year):
  print('{}is a leapyear.'.format(year))    
else:
     print('{}is a not leapyear.'.format(year)) 