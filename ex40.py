class Song(object):
    """description"""
    def __init__(self, lyrics):
        """docstring for __init__"""
        self.lyrics = lyrics

    def sing_me_a_song(self):
        """docstring for sing_me_a_song"""
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
    "I don`t want to get sued",
    "So I`ll stop right there"])

bulls_on_parade = Song(["They rally around the family",
    "With pockets full of shells"])

happy_bday.sing_me_a_song()
            
bulls_on_parade.sing_me_a_song()
