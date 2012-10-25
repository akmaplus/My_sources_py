# -*- coding: cp1251 -*-
'''
    reduce() - ��������� - ������������, ���������������� ����������, ������..
'''

lst = range(1, 11)   #������

def add(counter, new_value):      #�-��� ������������ ���� ��������, ������������(��������) � �������� ��������
    return counter + new_value
print reduce(add, lst)            #���������� ����� ����

f = lambda counter, new_value : counter + new_value    #����������, �������
print reduce(f, lst)                                   #���������� ����� ����

print reduce(lambda counter, new_value : counter + new_value,  lst )  #��� ������, �������������� - ���������� ����� ����

def Sum(seq):  #��������� ��������� (����������� �-��� ������ �-���)
    def add(counter, new_value): return counter + new_value 
    return reduce(add, seq, 0)
print Sum(lst)  #���������� ����� ����

def Sum(seq):  #��� ���������, ��������� ������
    return reduce(lambda counter, new_value : counter + new_value, seq, 0)
print Sum(lst)  #���������� ����� ����

Sum = lambda seq: reduce(lambda counter, new_value : counter + new_value, seq, 0)  #��� ������, ������ ����� ������� ;)
print Sum(lst)  #���������� ����� ����


import os, stat

#������� ��������� ������������ ������ ������ � ��������
def Files(path):
    return reduce(lambda acc,new: acc+new,  #���������� ������ ������������ ������� � ����
           map(lambda (r,ds,fs):   #������� ������ ����� � ������� - ������� ������ (r,ds,fs) "�����"
           map(lambda f: os.path.join(r,f), fs), os.walk(path) ) )  #������� ����� (fs) � ����� 

#��������� ����� ���� ������ �� ������ - ��������������
print reduce(lambda cntr,fn: cntr + os.stat(fn)[stat.ST_SIZE], Files("c:\\pypy"), 0)

#������ ������� �������� ����� ������ - ���������: �������, ���_�����_���_�����
f = lambda cntr,fn: cntr + os.stat(fn)[stat.ST_SIZE]
#��������� ����� ���� ������ �� ������, ��������� ������
print reduce(f, Files("c:\\pypy"), 0)
