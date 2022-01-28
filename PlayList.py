from collections import deque
import time

#TODO add shuffle decorator that plays songs at random
#TODO add tests for ALL methods
#TODO allow iteration over whole track list using for-in loop
class PlayList():
    def __init__(self):
        self.previous = deque()
        self.current = None
        self.next = deque()

    def add(self,song):
        self.next.append(song)
        if not self.current:
            self.current = song

    #TODO if removing last song of PlayList, set self.current to None
    def remove(self,song):
        try:
            self.previous.pop(song)
        except(ValueError):
            self.next.pop(song)
        finally:
            raise ValueError('Song Not Found')

    def __add__(self,other):
        for song in other:
            self.add(song)

    def play(self):
        if not self.current:
            try:
                self.current = self.next.popleft()
            except(ValueError):
                print('Play List Over')

        while len(self.next) > 0:
            print(f'Now Playing: {self.current.title}')
            time.sleep(self.current.duration)




        

class Song():
    def __init__(self,title,artist,duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def __eq__(self,other):
        return (
            self.title == other.title
            and self.artist == other.artist
            and self.duration == other.duration
        )
