import pygame
import button

from pygame.locals import *

pygame.mixer.init()
pygame.mixer.music.load('intro.mp3')
pygame.mixer.music.play()

pygame.init()

SCREEN_HEIGHT = 360
SCREEN_WIDTH = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Vampire Diries')

bg = pygame.image.load('go.jpg')
bg = pygame.transform.scale(bg ,(SCREEN_WIDTH , SCREEN_HEIGHT )).convert_alpha()


start_img = pygame.image.load('start.png').convert_alpha()
exit_img = pygame.image.load('exit.png').convert_alpha()


start_button = button.Button(180, -30, start_img, 0.2)
exit_button = button.Button(180, 120, exit_img, 0.2)



run = True
while run:
	pygame.init()
	
	screen.blit(bg , (0 ,0))
	if start_button.draw(screen):
		exec(open('main.py').read())
	if exit_button.draw(screen):
		run = False


	for event in pygame.event.get():
		
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit() 