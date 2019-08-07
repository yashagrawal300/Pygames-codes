import pygame
import time
pygame.init()
gameDisplay=pygame.display.set_mode((1000,1000))
#increase speed and fps to make it faster 
fps=100
speed=150
clock=pygame.time.Clock()

gameExit=False
while not gameExit:
	for red in range(0,255,speed):
		for green in range(0,255,speed):
			for blue in range(0,255,speed):
				gameDisplay.fill((255,255,255))
				font = pygame.font.SysFont("comicsansms", 32)
				pygame.draw.rect(gameDisplay,(red,green,blue),[100,200,500,700])
				pygame.draw.circle(gameDisplay,(red,0,0),[135,1000],70)
				pygame.draw.circle(gameDisplay,(0,green,0),[320,1000],70)
				pygame.draw.circle(gameDisplay,(0,0,blue),[505,1000],70)
				text = font.render('red='+str(red)+'  green='+str(green)+'  blue='+str(blue),True,(250,100,100))
				title=font.render('WATCH 16 MILLION COLOURS ',True,(0,0,0))
				gameDisplay.blit(text,[100,150])
				gameDisplay.blit(title,[100,0])
				clock.tick(fps)
				pygame.display.update()
	time.sleep(3)
	quit()
