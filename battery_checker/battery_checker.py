from collections.abc import Sequence

import psutil
import pygame
import time

def get_battery_percentage():
    battery = psutil.sensors_battery()
    return battery.percent if battery else None

def play_song(song_path):
    pygame.mixer.init()
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play()

def main():
    # Replace 'your_song.mp3' with the path to your song file
    song_path = 'your_song.mp3'

    while True:
        battery_percentage = get_battery_percentage()

        if battery_percentage is not None:
            print(f'Battery Percentage: {battery_percentage}%')

            if battery_percentage < 95:
                print('Battery is below 50%. Playing song...')
                play_song(song_path)

        # Check every 5 minutes
        time.sleep(30)

if __name__ == "__main__":
    main()
