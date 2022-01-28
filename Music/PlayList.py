from collections import deque
import time
from Music.Songs import Song

#TODO add shuffle decorator that plays songs at random
#TODO add tests for ALL methods
#TODO allow iteration over whole track list using for-in loop
class PlayList():
    def __init__(self):
        self.track_list = {
            'previous': deque(),
            'next': deque()
        }
        self.previous = deque()
        self.current = None
        self.next = deque()

    def add(self,song):
        self.track_list['next'].append(song)
        if not self.current:
            self.current = song

    #TODO if removing last song of PlayList, set self.current to None
    def remove(self,song):
        try:
            self.track_list['previous'].pop(song)
        except(ValueError):
            self.track_list['next'].pop(song)
        finally:
            raise ValueError('Song Not Found')

    def __add__(self,other):
        for song in other:
            self.add(song)

    def play(self):
        if not self.current:
            try:
                self.current = self.track_list['next'].popleft()
            except(ValueError):
                print('Play List Over')

        while len(self.next) > 0:
            print(f'Now Playing: {self.current.title}')
            time.sleep(self.current.duration)

    #TODO handle errors caused by next deque being empty when called
    #TODO make sure current is not None before appending to previous
    #TODO add tests to make sure track order is maintained when called
    def next(self):
        self.track_list['previous'].append(self.current)
        self.current = self.track_list['next'].popleft()

    #TODO handle errors caused by previous deque being empty when called
    #TODO make sure current is not None before appending to track_list
    #TODO add tests to make sure track order is maintained when called
    def back(self):
        self.track_list['next'].append(self.current)
        self.current = self.track_list['previous'].pop()

