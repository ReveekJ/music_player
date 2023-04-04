# ОБЯЗАТЕЛЬНО ДОЛЖЕН БЫТЬ УСТАНОВЛЕН VLC НА УСТРОЙСТВЕ!!!
import vlc
from mutagen.mp3 import MP3
from mutagen.mp4 import MP4
from mutagen.wave import WAVE
import time


class AudioVLC:

    def __init__(self, path_to_audio: str):
        self.audio = path_to_audio

    # def get_name(self):
    #     return self.audio[:self.audio.find('.')]

    def get_extension(self):
        return self.audio[self.audio.find('.'):]

    def get_len(self):
        if self.get_extension() == '.mp3':
            return MP3(self.audio).info.length
        elif self.get_extension() == '.mp4':
            return MP4(self.audio).info.length
        elif self.get_extension() == '.wav':
            return WAVE(self.audio).info.length
        else:
            raise ValueError('Неизвестное расширение аудио')

    def play_audio(self):
        player = vlc.MediaPlayer(self.audio)
        player.play()
        time.sleep(self.get_len())
