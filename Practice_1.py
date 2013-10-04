# -*- encoding: utf-8 -*-
""" Знакогенератор"""

cort1 = ('*',' ',' ',' ',' ',' ',' ',' ',)
cort2 = (' ',' ',' ',' ',' ',' ',' ','*',)
cort3 = ('*',' ',' ',' ',' ',' ',' ','*',)
cort4 = ('*','*','*','*','*','*','*','*',)

init = 2

if init == 1:
     print '\n', cort1
     print '\n', cort1
     print '\n', cort1
     print '\n', cort1
     print '\n', cort1
     print '\n', cort1
     print '\n', cort1
     print '\n', cort1
elif init == 2:
     print '\n', cort4
     print '\n', cort2
     print '\n', cort2
     print '\n', cort4
     print '\n', cort1
     print '\n', cort1
     print '\n', cort1
     print '\n', cort4
elif init == 3:
     print '\n', cort4
     print '\n', cort2
     print '\n', cort2
     print '\n', cort4
     print '\n', cort2
     print '\n', cort2
     print '\n', cort2
     print '\n', cort4
elif init == 4:
     print '\n', cort3
     print '\n', cort3
     print '\n', cort3
     print '\n', cort4
     print '\n', cort2
     print '\n', cort2
     print '\n', cort2
     print '\n', cort2
elif init == 5:
     print '\n', cort4
     print '\n', cort1
     print '\n', cort1
     print '\n', cort4
     print '\n', cort2
     print '\n', cort2
     print '\n', cort2
     print '\n', cort4
elif init == 6:
     print '\n', cort4
     print '\n', cort1
     print '\n', cort1
     print '\n', cort4
     print '\n', cort3
     print '\n', cort3
     print '\n', cort3
     print '\n', cort4
elif init == 7:
     print '\n', cort4
     print '\n', cort2
     print '\n', cort2
     print '\n', cort2
     print '\n', cort2
     print '\n', cort2
     print '\n', cort2
     print '\n', cort2
elif init == 8:
     print '\n', cort4
     print '\n', cort3
     print '\n', cort3
     print '\n', cort4
     print '\n', cort3
     print '\n', cort3
     print '\n', cort3
     print '\n', cort4
elif init == 9:
     print '\n', cort4
     print '\n', cort3
     print '\n', cort3
     print '\n', cort4
     print '\n', cort2
     print '\n', cort2
     print '\n', cort2
     print '\n', cort4
elif init == 0:
     print '\n', cort4
     print '\n', cort3
     print '\n', cort3
     print '\n', cort3
     print '\n', cort3
     print '\n', cort3
     print '\n', cort3
     print '\n', cort4

else:
     print 'Bad init'


""" Склонятор"""



def humanizer(x,**kwargs)
try:
if x % 10 == 0 or  x % 10 == 9 or x % 10 == 8 or x % 10 == 7 or x % 10 == 6 x % 10 == 5:
      pref = 'ов'
      s = kwargs[x] + pref

elif x % 10 == 2 or x % 10 == 3 or x % 10 == 4:
      pref = 'a'
      s = kwargs[x] + pref
else:
      s = kwargs[x]
      
      except:
         print 'error detected'
return 1



"""месяц"""

dict = { 'январь' : 1, 'февраль' : 2, 'март' : 3, 'апрель' : 4, 'май' : 5, 'июнь' : 6, 'июль' : 7, 'август' : 8, 'сентябрь' : 9, 'октябрь' : 10, 'ноябрь' : 11, 'декабрь' : 12}
print dict[raw_input()]


""" константы"""

dict = { 'pi' : '3.1434653464'}
arg1 = raw_input()
arg2 = raw_input()
dict2 = {arg1: arg2}
s = ' '
for i in range(0,dict2[arg1]):
      s = s + dict[arg1][i]
    


