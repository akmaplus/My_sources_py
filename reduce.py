# -*- coding: cp1251 -*-
'''
    reduce() - агрегация - суммирование, структурирование информации, прочее..
'''

lst = range(1, 11)   #список

def add(counter, new_value):      #ф-ция суммирования двух значений, аккумулятора(счетчика) и текущего значения
    return counter + new_value
print reduce(add, lst)            #вычисление суммы ряда

f = lambda counter, new_value : counter + new_value    #аналогично, лямбдой
print reduce(f, lst)                                   #вычисление суммы ряда

print reduce(lambda counter, new_value : counter + new_value,  lst )  #все вместе, однострочником - вычисление суммы ряда

def Sum(seq):  #используя замыкания (определение ф-ции внутри ф-ции)
    def add(counter, new_value): return counter + new_value 
    return reduce(add, seq, 0)
print Sum(lst)  #вычисление суммы ряда

def Sum(seq):  #без замыкания, используя лямбду
    return reduce(lambda counter, new_value : counter + new_value, seq, 0)
print Sum(lst)  #вычисление суммы ряда

Sum = lambda seq: reduce(lambda counter, new_value : counter + new_value, seq, 0)  #все вместе, лямбда редюс лямбдой ;)
print Sum(lst)  #вычисление суммы ряда


import os, stat

#функция генерация рекурсивного списка файлов в каталоге
def Files(path):
    return reduce(lambda acc,new: acc+new,  #объединяем группы разрозненных списков в один
           map(lambda (r,ds,fs):   #обходим списки папок с файлами - получая тройки (r,ds,fs) "папок"
           map(lambda f: os.path.join(r,f), fs), os.walk(path) ) )  #обходим файлы (fs) в папке 

#вычисляем сумму всех файлов из списка - однострочником
print reduce(lambda cntr,fn: cntr + os.stat(fn)[stat.ST_SIZE], Files("c:\\pypy"), 0)

#лямбда функция подсчета суммы файлов - аргументы: счетчик, имя_файла_для_счета
f = lambda cntr,fn: cntr + os.stat(fn)[stat.ST_SIZE]
#вычисляем сумму всех файлов из списка, используя лямбду
print reduce(f, Files("c:\\pypy"), 0)
