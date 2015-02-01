'''
Created on Jan 31, 2015

@author: nanci
'''

class Multimedia:
    '''
    Main class for Movie, Song and VideoGame
    '''
    def __init__(self, duration, name, price):
        self.__duration = duration
        self.__name = name
        self.__price = price

    def getter_duration(self):
        return self.__duration
    
    def setter_duration(self, duration):
        self.__duration = duration

    def getter_var2(self):
        pass
    
    def setter_var2(self):
        pass

class Video(Multimedia):
    """
    TODO: ...
    """
    def __init__(self, duration, name, price):
        Multimedia.__init__(self, duration, name, price)
    

class Movie(Multimedia):
    """
    TODO: ...
    """
    def __init__(self, duration, price, name, year, director):
        Multimedia.__init__(self, duration, name)
        self.__year = year
        self.__director = director
    
class Song(Multimedia):
    """
    TODO: ...
    """
    def __init__(self, duration, price, name, artist, album):
        Multimedia.__init__(self, duration, name)
        self.__artist = artist
        self.__album = album
