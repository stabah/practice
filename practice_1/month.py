# -*- encoding: utf-8 -*-

def month(x)
try:
dict = { 'январь' : 1, 'февраль' : 2, 'март' : 3, 'апрель' : 4, 'май' : 5, 'июнь' : 6, 'июль' : 7, 'август' : 8, 'сентябрь' : 9, 'октябрь' : 10, 'ноябрь' : 11, 'декабрь' : 12}
print dict[x]
except:
         print 'error detected'
return 1
