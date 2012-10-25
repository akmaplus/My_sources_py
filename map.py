# -*- coding: cp1251 -*-

lst = [1,2,3]

for i in map(None, lst):                            #�������� ��������, ����� �-���
    print i

for i in map(lambda x: chr(x+64), lst):             #����� ������, ������� �� �� �-��� chr()
    print i

lst = ['A','B','C']

for i in map(lambda x: ord(x), lst):                #����� ������, ������� �� �� �-��� ord()
    print i



dct = {1:"a", 2:"b", 3:"c"}

for s in map(lambda x:x, dct.iteritems() ):         #����� - �������� ���������� ���� � ����
    print s


#����� ���������� ������ ������, ��������� � ������! ����������, ��� � ����

for s in map(lambda(x,y):(x,y), dct.iteritems() ):      
    print s


#������� ������ ��������(���) �� �������, ����������� ���� � �������� ��������

for s in map(lambda(x, y):"%s = %s" % (x,y), dct.iteritems() ):   
    print s



lst = [(1,2), (4,5)]                #������ ���(��������) 2-����

for (x, y) in lst:                  #����� � ������
    print x, y

lst = [(1,2,3), (6,7,8)]            #������ ���(��������) 3-����

for (x, y, z) in lst:               #����� � ������
    print x, y, z


#��� ���� �����, ��� � ����, � ������-�������, ��� �������� � map()

lst = [(1,2), (4,5)]
for s in map(lambda(x, y):"%s = %s" % (x,y), lst ):
    print s

lst = [(1,2,3), (6,7,8)]
for s in map(lambda(x, y, z):"%s - %s - %s" % (x,y,z), lst ):
    print s


lst = ["1","2","3"]     #������� ��������� ������, � �������� ��� - ������
print "\n".join(lst)    #��������� ����������� "\n", ��� ��������� string!


lst = [(1,2,3), (6,7,8)]

#���������� ������������, ������ � ���������������!
print "\n".join( map(lambda(x,y,z):"%s - %s - %s" % (x,y,z), lst ) )

#���� �����, �����������, � ���� �����
lf = lambda(x,y,z):"%s - %s - %s" % (x,y,z)
print "\n".join( map(lf, lst ) )


lst1 = [1,2,3]

#�������� ������ �������� ������ �� 2
lst2 = map(lambda x:x*2, lst1)

print lst1
print lst2
#������ �������������� � ���������������
print "-".join( map(lambda x:"%s"%x, lst2 ))


lst1 = [1,2,3] #���� ������� � ������ ����������
lst2 = [4,5,6]

def add(x, y): return x+y   #���������� ���� � ���������

#���������� �����������, �������� �������, ��������� ����� ������
lst3 = map(add, lst1, lst2)  

print lst1
print lst2
print lst3


lst1 = [1,2,3] #���� ������� � ������ ����������
lst2 = [4,5,6]
lst3 = [2,1,0]

def add(x, y, z): return x+y+z   #���������� ������ � ��������� �����

#���������� �����������, �������� �������, ��������� ����� ������
lst4 = map(add, lst1, lst2, lst3)  

print lst1
print lst2
print lst3
print lst4


lst = [1,2,3]
print [ chr(64+x) for x in lst ]


