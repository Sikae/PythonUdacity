'''
Created on Jan 31, 2015

@author: nanci
'''
import time

class Clock:
    '''
    This class if for all the types af clocks
    '''
    
 
    def __init__(self, colour, size):
        
        
        self.___colour = colour
        self.__size = size
        
    def get_colour(self):
        return self.___colour     

    def set_colour(self, colour):
        self.___colour = colour
        
    def get_size(self):
        return self.__size
    
    def set_size(self, size):
        self.__size = size
        
    def say_time(self):
        '''
        Print: time Day Month number hh:mm:ss year
        '''
        print(time.ctime())
        
    def __str__(self):
        return "Colour: " + self.___colour + " \nSize: " + self.__size

mySecondClock = Clock("yellow", "xl")
x = 5.0
class Watch(Clock):
    '''
    This class if for all the types af clocks
    '''
    
    def __init__(self, colour, size, gender, type):
        Clock.__init__(self, colour, size)
        self.__gender = gender
        self.__type = type
        
    def __str__(self):
        return Clock.__str__(self) + "\nGender: " + self.__gender + " \nType: " + self.__type    
        
# mine = Clock("red", "M")
# mine.___colour = "yellow"
# mine.say_time()
# print(mine.___colour)
# print(mine.__module__)
# print(mine.say_time.__doc__)
myClock = Clock("blue", "L")
print(myClock.__str__())
myWatch = Watch("black", "S", "Woman", "Sport")
myWatch.say_time()
print(myWatch)