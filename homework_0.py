'''
Created on Jan 31, 2015

@author: nanci
'''

class Multimedia:
    '''
    Main class for Movie, Song and VideoGame
    '''
    def __init__(self, duration, name):
        '''
        Constructor
        '''
        self.__duration = duration
        self.__name = name

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
    def __init__(self, duration, name):
        Multimedia.__init__(self, duration, name)
    

class Movie(Multimedia):
    """
    TODO: ...
    """
    def __init__(self, duration, name, year):
        Multimedia.__init__(self, duration, name)
        self.__year = year
    
class Song(Multimedia):
    """
    TODO: ...
    """
    def __init__(self, duration, name, artist, album):
        Multimedia.__init__(self, duration, name)
        self.__artist = artist
        self.__album = album
