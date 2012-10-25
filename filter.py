# -*- coding: cp1251 -*-

# ���������� ������ - �-��� ����. ���. ��������� � ����������� �� ��������
##def f(x): 
#    return (x%2 != 0)  and  (x%3 != 0)

#���������� �������� - ������������� ������ �-��� ��� ������ ��������
f = lambda x:(x%2!=0) and (x%3!=0)
print filter(f, range(2,25) )

#�������� ������, ���������� �������� ������ �����
lst = [1, u"1","a", 0xFFFFFFFF, 0.112, [1,2,3], {1:"12"}, (1,2,3), bytearray(), xrange(0,1), True ]

#���������� ������ �-��� ������ �������� - ���� �������� �����
f = lambda x: isinstance(x, int )

#��������� ������ �� �������, ������������� � �����-������� - ��� �������� �����
print filter(f, lst )

#������ ������������� ������-������� ������������ �������
f = lambda y: lambda x: isinstance(x,y)

#�������� ������ �������, ��������� ������ "��������" ��� �������� ����������,
#������ �-��� (���������� "��������") ���������� ������� filter(  ��� ������ ������
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

