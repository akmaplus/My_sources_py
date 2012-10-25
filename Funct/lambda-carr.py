# -*- coding: utf-8 -*-

s = u"2 + 4"
print eval(s)                       #вычислить выражение

s = u"lambda x, y : x + y"          #лямбда выражение
print eval(s)                       #вычилить лямбда выражение  - по сути ничего - параметры ф-ции не переданы - печать адреса ф-ции

s = u"lambda x, y : x + y"          #лямбда выражение
print eval(s)(1, 2)                 #вычилить лямбда выражение - параметры идут следом


op = u"*"                                     #операция
funct = u"lambda x, y : x " + op + " y"       #лямбда выражение
print eval(s)(3, 4)                           #вычилить лямбда выражение - параметры идут следом




def prn(x, y):                                #ф-ция печати вх. параметров
    print "x=%s y=%s" % (x,y)

funct = lambda x : lambda y : prn(x, y)       #карринг выражение

funct( 2 ) ( 3 )              #использование каррирующей ф-ции


def fnx(x):                   #развернутое представление карринг ф-ции
    def fny(y):               #опред. ф-цию
        return prn(x, y)      #вычисл. и возрат результ.
    return fny                #проброс его сюда(в виде реально исполнен. ф-ции) и возврат наружу

funct( 7 ) ( 9 )              #использование каррирующей ф-ции