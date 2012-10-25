# -*- coding: utf-8 -*-

lst = [123,12,5345,3,1123,344]   #новый список

lst = sorted(lst)   #сортируем список в порядке возрастания членов
print lst           #печать

lst = sorted(lst, reverse=True)     #сортируем список в порядке убывания членов
print lst                           #печать


lst = list( [123,12,5345,3,1123,344] )  #новый список
lst.sort()    #сортировка на месте, без созд. нового списка, нельзя это делать вышестоящей строке
print lst     #печать

print sorted( [123,12,5345,3,1123,344] )  #здесь все можно, в одной строке

dct = {67:"D", 66:"C", 65:"B", 68:"F", 64:"A", 20:"S", 22:"L"}   #словарь 
print map(lambda x:dct[x], dct)               #печать словаря без ключей
print map(lambda x:dct[x], sorted(dct))       #печать отсортированного по ключам словаря

print map(lambda x:dct[x], sorted(dct, key=lambda x:dct[x]))  #сортировка словаря по значениям и печать

#lst = [[7,0],[10,1],[10,2],[10,3],[10,4],[3,0],[1,0]]  #новый список с элементами списками
lst = [(7,0),(10,1),(10,2),(10,3),(10,4),(3,0),(1,0)]  #с элементами парами - аналогично списку
print sorted(lst, key=lambda x:x[0])                   #сортируем по первому элементу списка
#после печати видим - сортировка стабильна - сохр. порядок следования эл. с одинаковыми знач.

#сортировка старым способ используя параметр cmp - так не желательно делать - устарело в 3.х
print sorted([3,0,6,1,2,4,3], cmp=lambda x,y:x-y)
print sorted([3,0,6,1,2,4,3], cmp=lambda x,y:y-x)

######################## ниже пользовательская сортировка ########################

numeric_compare = lambda x,y:x-y
reverse_numeric = lambda x,y:y-x

def cmp_to_key(mycmp):
    class K(object):
        def __init__(self, obj, *args):
            self.obj = obj
            print ":",
        def __lt__(self, other):
            print "lt",
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            print "gt",
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            print "eq",
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            print "le",
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            print "ge",
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            print "ne",
            return mycmp(self.obj, other.obj) != 0
    print ">",
    return K

lst = [100,0,7,5,3,17,3,9,1]
print sorted(lst, key=cmp_to_key(reverse_numeric))
print sorted(lst, key=cmp_to_key(numeric_compare))

