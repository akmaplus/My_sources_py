# -*- coding: cp1251 -*-

# простейший случай - ф-ция возр. лог. результат в зависимости от значения
##def f(x): 
#    return (x%2 != 0)  and  (x%3 != 0)

#нормальная практика - использование лямбда ф-ции для оценки значения
f = lambda x:(x%2!=0) and (x%3!=0)
print filter(f, range(2,25) )

#тестовый список, содержащий значения разных типов
lst = [1, u"1","a", 0xFFFFFFFF, 0.112, [1,2,3], {1:"12"}, (1,2,3), bytearray(), xrange(0,1), True ]

#простейший случай ф-ции оценки значения - если значение целое
f = lambda x: isinstance(x, int )

#фильтруем список по условию, поставленному в лябда-функции - все короткие целые
print filter(f, lst )

#делаем универсальную лямбда-функцию использующую карринг
f = lambda y: lambda x: isinstance(x,y)

#вызываем лямбда функцию, передавая первой "матрешке" тип значения фильтрации,
#вторая ф-ция (внутренняя "матрешка") вызывается функций filter(  при обходе списка
print filter( f(int),       lst )
print filter( f(long),      lst )
print filter( f(float),     lst )
print filter( f(str),       lst )
print filter( f(unicode),   lst )
print filter( f(bool),      lst )
print filter( f(list),      lst )
print filter( f(dict),      lst )
print filter( f(tuple),     lst )
print filter( f(bytearray), lst )
print filter( f(xrange),    lst )
print filter( f(object),    lst )

