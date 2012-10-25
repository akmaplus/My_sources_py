# -*- coding: utf-8 -*-

#начиная с 2.4 при объявлении класса в скобках указывать object (3.хх можно не указывать, там передача неявная)
class simple( object ):
    #статическое объявление переменных - ТАК не нужно делать!
    '''
    a = "simple"
    b = ["simple"]
    c = None
    '''
    #статическое объявление закрытых переменных - ТАК не нужно делать!
    '''
    __d = ("simple")
    __e = {"simple":"simple"}
    __f = None
    '''

    def __init__(self): #конструктор экземляра класса
        #динамическое объявление переменных класса в конструкторе - ПРАВИЛЬНО!
        self.a = "simple"
        self.b = ["simple"]
        self.c = None

        #динамическое объявление закрытых переменных класса в конструкторе - ПРАВИЛЬНО!
        self.__d = ("simple")
        self.__e = {"simple":"simple"}
        self.__f = None

    def Say(self):
        print self.a, self.b, self.c,   self.__d, self.__e, self.__f

    def D(self):          #простой метод класса, возращает закрытую переменную self.__d
        return self.__d

    @property             # ТАК превращаем метод, в свойство "только для чтения"
    def E(self):          #аналогично, метод для возрата self.__e
        return self.__e


print __name__    #служебная переменная-флаг, тип запуска текущего исходника - как модуль или основной
print __file__    #имя файла этого исходника

if (__name__=="__main__"):   # исполнить, все что ниже, ЕСЛИ, файл неявляется модулем

    obj = simple()           #создаем объект
    obj.Say()                #вызываем метод объекта - печатаем переменные объекта

    simple.Say(obj)          #вызываем метод объекта из класса, передавая ОБЯЗАТЕЛЬНЫЙ объект класса
    simple.Say(simple())     #аналогично, создаем объект налету

    print obj.a, obj.b, obj.c     #вполне реальное применение! это НЕ свойства! данные класса!

    #print obj.__d, obj.__e, obj.__c    # ТАК нельзя! ошибка

    # ТАК можно, громозко, неудобно - на случай, действительной необходимости  (\ слэш продолжение строки)
    print obj._simple__d, \
          obj._simple__e, \
          obj._simple__f


    print obj.D(),   \
          obj.E

    # ТАК допустимо, менять значение данных, экземпляра класса
    obj.a = {}
    obj.b = []
    obj.c = ()
    
    #obj.E = {}    #ошибка, свойство, "только для чтения"
    obj.Say()      #печатаем переменные объекта (данные объекта)        