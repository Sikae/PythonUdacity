'''
Created on Jan 31, 2015

@author: nanci
'''

class Multimedia:
    '''
    Main class for Movie, Song and VideoGame
    '''
    def __init__(self, duration):
        '''
        Constructor
        '''
        self.__duration = duration

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
    def __init__(self, duration):
        Multimedia.__init__(self, duration)
    

class Movie(Multimedia):
    """
    TODO: ...
    """
    def __init__(self, duration):
        Multimedia.__init__(self, duration)
    
class Song(Multimedia):
    """
    TODO: ...
    """
    def __init__(self, duration):
        Multimedia.__init__(self, duration)
