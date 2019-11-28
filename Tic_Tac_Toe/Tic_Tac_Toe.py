import pygame
import random
import time

pygame.init()
width = 300
height = 300
display = pygame.display.set_mode((width, 500))

score_com  = 0
score_human = 0
score_tie = 0

def playground(width, height):

    pygame.draw.line(display, (255, 255, 255), (0, height / 3), (width, height / 3), 3)
    pygame.draw.line(display, (255, 255, 255), (0, (height / 3) * 2), (width, (height / 3) * 2), 3)
    pygame.draw.line(display, (255, 255, 255), (width / 3, 0), (width / 3, height), 3)
    pygame.draw.line(display, (255, 255, 255), ((width / 3) * 2, 0), ((width / 3) * 2, height), 3)
    pygame.draw.polygon(display, (255, 0, 255), [(0, 0), (300, 0), (0, 0), (0, 300), (0, 300), (300, 300), (300, 300), (300, 0)], 10)

moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
s = [(0, 0), (100, 0), (200, 0), (0, 100), (100, 100), (200, 100), (0, 200), (100, 200), (200, 200)]
comp_list = []
human_list = []


def process_comp(comp_list):
    win_list = [[1, 2, 3], [1, 5, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [3, 5, 7], [4, 5, 6], [7, 8, 9]]
    for i in range(len(win_list)):
        count = 0
        for j in range(len(win_list[i])):
            for k in range(len(comp_list)):
                if comp_list[k] == win_list[i][j]:
                    count += 1
        if count == 3:
            return 1


def process_human(human_list):
    win_list = [[1, 2, 3], [1, 5, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [3, 5, 7], [4, 5, 6], [7, 8, 9]]
    for i in range(len(win_list)):
        count_human = 0
        for j in range(len(win_list[i])):
            for k in range(len(human_list)):
                if human_list[k] == win_list[i][j]:
                    count_human += 1
        if count_human == 3:
            return 1


def X(x, y):
    pygame.draw.line(display, (255, 255, 255), (25 + x, 25 + y), (75 + x, 75 + y), 2)
    pygame.draw.line(display, (255, 255, 255), (25 + x, 75 + y), (75 + x, 25 + y), 2)


def human(number):
    Z(s[number - 1][0], s[number - 1][1])
    moves.remove(number)
    human_list.append(number)
    process_human(human_list)
    pygame.display.update()


def Z(x, y):
    pygame.draw.circle(display, (255, 255, 255), (50 + x, 50 + y), 30, 2)


while True:

    for i in range(len(moves)):
        playground(width, height)
        player_comp = random.choice(moves)
        X(s[player_comp - 1][0], s[player_comp - 1][1])
        moves.remove(player_comp)
        comp_list.append(player_comp)
        process_comp(comp_list)
        font = pygame.font.SysFont("comicsansms", 30)
        text_won = font.render('Won  ' + str(score_human), True, (255, 255, 255))
        text_lost = font.render('Lost  ' + str(score_com), True, (255, 0, 0))
        text_tie = font.render('Tie  ' + str(score_tie), True, (0, 255, 0))
        display.blit(text_lost, [100, 380])
        display.blit(text_won, [100, 340])
        display.blit(text_tie, [100, 420])
        pygame.display.update()
        if process_comp(comp_list) == 1:
            print('Computer Won')
            score_com +=1
            time.sleep(3)
            moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            s = [(0, 0), (100, 0), (200, 0), (0, 100), (100, 100), (200, 100), (0, 200), (100, 200), (200, 200)]
            comp_list = []
            human_list = []
            playground(width, height)
            pygame.display.update()
            break
        elif i == 4:
            print('Tie')
            score_tie+=1
            time.sleep(3)
            break


        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_KP1:
                        human(1)
                        break
                    elif event.key == pygame.K_KP2:
                        human(2)
                        break
                    elif event.key == pygame.K_KP3:
                        human(3)
                        break
                    elif event.key == pygame.K_KP4:
                        human(4)
                        break
                    elif event.key == pygame.K_KP5:
                        human(5)
                        break
                    elif event.key == pygame.K_KP6:
                        human(6)
                        break
                    elif event.key == pygame.K_KP7:
                        human(7)
                        break
                    elif event.key == pygame.K_KP8:
                        human(8)
                        break
                    elif event.key == pygame.K_KP9:
                        human(9)
                        break

            else:
                continue
            break
        if process_human(human_list) == 1:
            print('Human Won')
            score_human+=1
            time.sleep(3)
            break


    display.fill((0, 0, 0))
    moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    s = [(0, 0), (100, 0), (200, 0), (0, 100), (100, 100), (200, 100), (0, 200), (100, 200), (200, 200)]
    comp_list = []
    human_list = []
    playground(width, height)
    font = pygame.font.SysFont("comicsansms", 30)
    text_won = font.render('Won  '+str(score_human), True, (255, 255, 255))
    text_lost = font.render('Lost  '+ str(score_com), True, (255,0,0))
    text_tie = font.render('Tie  '+ str(score_tie), True, (0,255,0))
    display.blit(text_lost, [100, 380])
    display.blit(text_won, [100, 340])
    display.blit(text_tie, [100, 420])

    pygame.display.update()

    pygame.display.update()
pygame.quit()
