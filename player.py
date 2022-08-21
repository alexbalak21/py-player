import eyed3
from playsound import playsound



class Tag:
    def __init__(self, title, artist, album) -> None:
        self.title = title
        self.artist = artist
        self.album = album

def show_info():
    audio = eyed3.load(".\\album\\01  Reise, Reise.mp3")
    print(audio.tag.artist)
    print(audio.tag.album)
    print(audio.tag.title)
    

playsound(".\\album\\01  Reise, Reise.mp3")
print('playing sound using  playsound')