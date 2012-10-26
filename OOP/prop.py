# -*- coding: utf-8 -*-

class Test( object ):


    def __init__(self):
        self.__id = None

    #свойство реализованное лямбдой
    id = property ( lambda self: self.__id )

    
    #свойство реализованное методом
    def getid( self ):
        return self.__id

    Id = property( getid )

    #аналогично, методом, используя декоратор
    @property
    def ID( self ):
        return self.__id


if (__name__=="__main__"):

    obj = Test()

    print obj.id
    print obj.Id
    print obj.ID
