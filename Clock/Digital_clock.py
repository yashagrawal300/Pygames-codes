import pygame
import time
from datetime import date

pygame.init()
display = pygame.display.set_mode((400, 400))

x = 125
y = 185


def up(x, y):
    pygame.draw.line(display, (255, 255, 255), (x, y), (x + 10, y), 3)


def top_left(x, y):
    pygame.draw.line(display, (255, 255, 255), (x, y), (x, y + 10), 3)


def top_right(x, y):
    pygame.draw.line(display, (255, 255, 255), (x + 10, y), (x + 10, y + 10), 3)


def middle(x, y):
    pygame.draw.line(display, (255, 255, 255), (x, y + 10), (x + 10, y + 10), 3)


def bottom_left(x, y):
    pygame.draw.line(display, (255, 255, 255), (x, y + 10), (x, y + 20), 3)


def bottom_right(x, y):
    pygame.draw.line(display, (255, 255, 255), (x + 10, y + 10), (x + 10, y + 20), 3)


def down(x, y):
    pygame.draw.line(display, (255, 255, 255), (x, y + 20), (x + 10, y + 20), 3)


def one(x, y):
    top_right(x, y)
    bottom_right(x, y)


def two(x, y):
    up(x, y)
    top_right(x, y)
    middle(x, y)
    bottom_left(x, y)
    down(x, y)


def three(x, y):
    up(x, y)
    top_right(x, y)
    bottom_right(x, y)
    middle(x, y)
    down(x, y)


def four(x, y):
    top_left(x, y)
    middle(x, y)
    top_right(x, y)
    bottom_right(x, y)


def five(x, y):
    up(x, y)
    top_left(x, y)
    middle(x, y)
    bottom_right(x, y)
    down(x, y)


def six(x, y):
    top_left(x, y)
    bottom_right(x, y)
    down(x, y)
    bottom_left(x, y)
    middle(x, y)


def seven(x, y):
    top_right(x, y)
    bottom_right(x, y)
    up(x, y)


def eight(x, y):
    up(x, y)
    middle(x, y)
    top_left(x, y)
    top_right(x, y)
    bottom_left(x, y)
    bottom_right(x, y)
    down(x, y)


def nine(x, y):
    up(x, y)
    middle(x, y)
    top_right(x, y)
    top_left(x, y)
    bottom_right(x, y)
    down(x, y)


def zero(x, y):
    up(x, y)
    top_right(x, y)
    top_left(x, y)
    down(x, y)
    bottom_right(x, y)
    bottom_left(x, y)


def show(number, x, y):
    if number == 0:
        zero(x, y)
    elif number == 1:
        one(x, y)
    elif number == 2:
        two(x, y)
    elif number == 3:
        three(x, y)
    elif number == 4:
        four(x, y)
    elif number == 5:
        five(x, y)
    elif number == 6:
        six(x, y)
    elif number == 7:
        seven(x, y)
    elif number == 8:
        eight(x, y)
    elif number == 9:
        nine(x, y)


while True:
    pygame.draw.circle(display, (255, 0, 0), (x+79, y+6), 150, 3)
    t = time.localtime()
    hr = time.strftime("%H", t)
    minute = time.strftime("%M", t)
    sec = time.strftime('%S', t)
    today = date.today()
    d2 = today.strftime("%B %d, %Y")
    font = pygame.font.SysFont("comicsansms", 25)
    text = font.render(d2, True, (255,255,0))
    display.blit(text, [x-12, y-70])
    hr = list(hr)
    minute = list(minute)
    sec = list(sec)
    show(int(hr[0]), x, y+5)
    show(int(hr[1]), x + 20, y+5)
    pygame.draw.circle(display, (255, 0, 0), (x+45, y+8), 2, 1)
    pygame.draw.circle(display, (255, 0, 0), (x + 45, y+23), 2, 1)
    show(int(minute[0]), x + 60, y+5)
    show(int(minute[1]), x + 85, y+5)
    pygame.draw.circle(display, (255, 0, 0), (x + 110, y + 8), 2, 1)
    pygame.draw.circle(display, (255, 0, 0), (x + 110, y + 23), 2, 1)
    show(int(sec[0]), x + 125, y+5)
    show(int(sec[1]), x + 145, y+5)
    pygame.display.update()
    display.fill((0, 0, 0))

time.sleep(12)
quit()
