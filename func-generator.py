# -*- coding: cp1251 -*-


def testG():   #�-��� ��������� - �����������
    yield 1    #��� 1
    yield 2    #��� 2  �� ���� ����� ���������� � ���������� ������������ ����. ����������, ������ �������� ���, ��������� ���
    yield 3    #��� 3
    yield 4    #��� 4
    yield 5    #��� 5


def issimple(x):                 #�-��� ����. ������ ���� �������� - ������� �����
    for k in range( 2, x/2):
        if x % k == 0:
            return False
    return True


def simple(n):   #�-��� ��������� - ������������
    k = 2
    while k<n:
        if issimple(k):    #���� ����� ������� ��������� ��� �����, � ���������� ��� ���������, ����� � ��������� ����� ���������� ��������, ��� �����, ����� ���������
            yield k        #������ ����� �����
        k += 1             #��������� �-��� - ��� �� ������� � ������� �-��� ��������� ���� ��� � ��������� �� ������
        print "-", k, "-"



for i in testG():   #������������� �-��� ���������� - ������ ��� ��������. ����� �-��� ��� ��������� ������. ����.
    print i

print "\n"



for i in simple(10):  #������������� �-��� ����������
    print i