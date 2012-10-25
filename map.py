# -*- coding: utf-8 -*-

lst = [1,2,3]

for i in map(None, lst):                            #передача напрямую, минуя ф-цию
    print i

for i in map(lambda x: chr(x+64), lst):             #через лямбду, вызывая из неё ф-цию chr()
    print i

lst = ['A','B','C']

for i in map(lambda x: ord(x), lst):                #через лямбду, вызывая из неё ф-цию ord()
    print i



dct = {1:"a", 2:"b", 3:"c"}

for s in map(lambda x:x, dct.iteritems() ):         #здесь - передача аргументов один в один
    print s


#когда параметров больше одного, параметры в скобки! аналогично, что и выше

for s in map(lambda(x,y):(x,y), dct.iteritems() ):      
    print s


#обходим массив кортежей(пар) из словаря, преобразуем пары в строчный параметр

for s in map(lambda(x, y):"%s = %s" % (x,y), dct.iteritems() ):   
    print s



lst = [(1,2), (4,5)]                #список пар(кортежей) 2-ками

for (x, y) in lst:                  #обход и печать
    print x, y

lst = [(1,2,3), (6,7,8)]            #список пар(кортежей) 3-ками

for (x, y, z) in lst:               #обход и печать
    print x, y, z


#все тоже самое, что и выше, в лямбде-функции, при передаче в map()

lst = [(1,2), (4,5)]
for s in map(lambda(x, y):"%s = %s" % (x,y), lst ):
    print s

lst = [(1,2,3), (6,7,8)]
for s in map(lambda(x, y, z):"%s - %s - %s" % (x,y,z), lst ):
    print s


lst = ["1","2","3"]     #слияние элементов списка, в строчный тип - строку
print "\n".join(lst)    #используя разделитель "\n", тип элементов string!


lst = [(1,2,3), (6,7,8)]

#фактически однострочник, печать с форматированием!
print "\n".join( map(lambda(x,y,z):"%s - %s - %s" % (x,y,z), lst ) )

#тоже самое, читабельней, в пару строк
lf = lambda(x,y,z):"%s - %s - %s" % (x,y,z)
print "\n".join( map(lf, lst ) )


lst1 = [1,2,3]

#умножаем каждое значение списка на 2
lst2 = map(lambda x:x*2, lst1)

print lst1
print lst2
#печать однострочником с форматированием
print "-".join( map(lambda x:"%s"%x, lst2 ))


lst1 = [1,2,3] #пара списков с целыми значениями
lst2 = [4,5,6]

def add(x, y): return x+y   #складываем пару и возращаем

#складываем поэлементно, значения списков, возращаем новый список
lst3 = map(add, lst1, lst2)  

print lst1
print lst2
print lst3


lst1 = [1,2,3] #пара списков с целыми значениями
lst2 = [4,5,6]
lst3 = [2,1,0]

def add(x, y, z): return x+y+z   #складываем тройку и возращаем сумму

#складываем поэлементно, значения списков, возращаем новый список
lst4 = map(add, lst1, lst2, lst3)  

print lst1
print lst2
print lst3
print lst4


lst = [1,2,3]
print [ chr(64+x) for x in lst ]


