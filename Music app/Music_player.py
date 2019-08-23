import pygame
import random

pygame.init()
current_song_value = 0
display = pygame.display.set_mode((600, 600))
# List of songs that are in the laptop
songs = ['Guess Whos Back.mp3', 'gym class.mp3', 'Eminem - Not Afraid(MP3_160K).mp3', 'Flo Rida - Whistle ['
                                                                                      'Official Video]('
                                                                                      'MP3_160K).mp3',
         'Lil Nas X - Old Town Road.mp3']
# List of songs that are going to show
song_names = ['Guess Whos Back', 'Gym class', 'Eminem - Not Afraid', 'Flo Rida - Whistle',
              'Lil Nas X - Old Town Road']
pause = 0


def song_list():
    # Printing the list of songs
    for i in range(len(song_names)):
        font = pygame.font.SysFont("Arial", 20)
        list_of_songs = font.render(str(i + 1) + '.  ' + song_names[i], True, (255, 255, 255))
        display.blit(list_of_songs, [40, 110 + 35 * i])
        pygame.display.update()


def current_song(current_song_value):
    # Printing the current song
    if current_song_value > len(songs) - 1:
        current_song(current_song_value % (len(songs)))
    else:
        font = pygame.font.SysFont("Arial", 25)
        current_play = font.render(song_names[current_song_value], True, (255, 255, 255))
        display.blit(current_play, [170, 375])
        pygame.display.update()


def play(current_song_value):
    # Playing the current music
    if current_song_value > len(songs) - 1:
        play(current_song_value % (len(songs)))
    else:
        pygame.mixer.music.set_endevent(pygame.USEREVENT + 1)
        pygame.mixer.music.load(songs[current_song_value])
        pygame.mixer.music.play()
        current_song(current_song_value)


# Change the font color

def frame():
    # List of songs
    font = pygame.font.SysFont("Arial", 45)
    list_of_songs = font.render('LIST OF SONGS', True, (255, 255, 255))
    display.blit(list_of_songs, [150, 30])

    # List of songs box
    pygame.draw.rect(display, (255, 0, 0), [30, 100, 310, 200], 2)

    # Current song box
    pygame.draw.rect(display, (255, 0, 255), [100, 340, 410, 100], 2)

    # Playing last song box
    font = pygame.font.SysFont("Arial", 25)
    list_of_songs = font.render('B', True, (255, 255, 255))
    display.blit(list_of_songs, [105, 480])
    pygame.draw.rect(display, (255, 0, 255), [100, 470, 30, 50], 2)

    # Pausing the song box
    list_of_songs = font.render('P', True, (255, 255, 255))
    display.blit(list_of_songs, [295, 480])
    pygame.draw.rect(display, (255, 0, 255), [100 + 190, 470, 30, 50], 2)

    # Playing next song box
    list_of_songs = font.render('N', True, (255, 255, 255))
    display.blit(list_of_songs, [485, 480])
    pygame.draw.rect(display, (255, 0, 255), [100 + 380, 470, 30, 50], 2)

    # Shuffling the song box
    font = pygame.font.SysFont("Arial", 20)
    list_of_songs = font.render('SHUFFLE', True, (255, 255, 255))
    display.blit(list_of_songs, [255, 555])
    pygame.draw.rect(display, (90, 123, 255), [100, 550, 410, 35], 2)

    # creating some designs
    for i in range(20):
        x = random.randint(0, 600)
        y = random.randint(0, 600)
        width = random.randint(0, 7)
        length = random.randint(0, 200)
        color = random.randint(0, 255)
        # Circles on screen
        pygame.draw.circle(display, (255 - color, 0 + color, 255), (x, y), 2, 1)

        # Right side bars
        pygame.draw.line(display, (255 - color, color, color), (575, 600), (575, length), width + 3)
        pygame.draw.line(display, (color, 255 - color, color), (570, 600), (570, 300 + length), width + 1)
        pygame.draw.line(display, (color, color, color), (565, 600), (565, 500 + length), width + 4)
        pygame.draw.line(display, (color, 255 - color, color), (560, 600), (560, 350 + length), width + 1)
        pygame.draw.line(display, (255 - color, color, 255 - color), (555, 600), (555, 400 + length), width + 4)
        pygame.draw.line(display, (255 - color, 255 - color, color), (550, 600), (550, 100 + length), width + 2)

        # Left side bars
        color = random.randint(0, 255)
        width = random.randint(0, 7)
        length = random.randint(0, 100)
        pygame.draw.line(display, (255 - color, 255 - color, color), (0, 600), (0, 400 + length), width)
        pygame.draw.line(display, (color, 255 - color, color), (5, 600), (5, length + 280), width + 1)
        pygame.draw.line(display, (color, color, color), (10, 600), (10, length + 550), width + 2)
        pygame.draw.line(display, (255 - color, 255 - color, 255 - color), (8, 600), (8, 550), width + 5)

    song_list()
    play(current_song_value)
    pygame.display.update()


count = 0

frame()

while True:
    for event in pygame.event.get():
        display.fill((0, 0, 0))
        if event.type == pygame.USEREVENT + 1:
            # Next songs when the current is done
            current_song_value += 1
            play(current_song_value)
            frame()
            song_list()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n or event.key == pygame.K_RIGHT:
                # If pressed N or right arrow key next song will be played
                current_song_value += 1
                play(current_song_value)
                frame()
                song_list()
            elif event.key == pygame.K_b or event.key == pygame.K_LEFT:
                # When B or left arrow key is  pressed the last song will played
                current_song_value -= 1
                play(current_song_value)
                frame()
                song_list()
            elif event.key == pygame.K_s:
                # When S is pressed it will shuffle
                current_song_value = random.randint(0, len(songs) - 1)
                play(current_song_value)
                frame()
                song_list()
            elif event.key == pygame.K_p or event.key == pygame.K_SPACE:
                # If P or Spsce bar is pressed then song will be paused
                if pause == 0:
                    # To pause the current song
                    pygame.mixer_music.pause()
                    pause += 1
                elif pause == 1:
                    # To unpause it
                    pygame.mixer_music.unpause()
                    pause -= 1
