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