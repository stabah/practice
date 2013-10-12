# -*- encoding: utf-8 -*-

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
