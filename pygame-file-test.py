import pygame
import os

pygame.init()

win = pygame.display.set_mode((1200,700))
pygame.display.set_caption("Image Color Picker")
img = None
run = True
clock = pygame.time.Clock()

font = pygame.font.Font('arial.ttf', 32)
text = font.render('Drag and drop an image to begin', True, (255,255,255))
font1 = pygame.font.Font('arial.ttf', 16)


def img_drop():
	global img
	if img.get_width() > img.get_height():
		if(img.get_width() > 1100):
			new_width = 1100
			new_height = 1100/img.get_width() * img.get_height()
			img = pygame.transform.scale(img,(new_width,new_height))
	else:
		if(img.get_height() > 700):
			new_height = 700
			new_width = 700/img.get_height() * img.get_width()
			img = pygame.transform.scale(img,(new_width,new_height))



while run:
	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.DROPFILE:
			img = pygame.image.load(os.path.join('', event.file))
			img_drop()
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_SPACE:
				win = pygame.display.set_mode((500,600))
	win.fill((0,0,0))
	if img:
		win.blit(img,(0,0))
		x,y = pygame.mouse.get_pos()
		print(x,y)
		if x < img.get_width() and y < img.get_height():
			colors = img.get_at((x,y))
			pygame.draw.rect(win,(colors[0],0,0),(1110,20,80,80))
			pygame.draw.rect(win,(0,colors[1],0),(1110,130,80,80))
			pygame.draw.rect(win,(0,0,colors[2]),(1110,240,80,80))
			pygame.draw.rect(win,(colors[0],colors[1],colors[2]),(1110,350,80,80))
			pygame.draw.rect(win,(255,255,255),(1110,20,80,80),1)
			pygame.draw.rect(win,(255,255,255),(1110,130,80,80),1)
			pygame.draw.rect(win,(255,255,255),(1110,240,80,80),1)
			pygame.draw.rect(win,(255,255,255),(1110,350,80,80),1)
			pygame.draw.circle(win,(colors[0],colors[1],colors[2]),(x,y),30,10)
			pygame.draw.circle(win,(0,0,0),(x,y),20,1)
			pygame.draw.circle(win,(0,0,0),(x,y),30,1)
			text = font1.render(f"Red: {colors[0]}", True, (255,255,255))
			textRect = text.get_rect()
			textRect.center = (1150,110)
			win.blit(text,textRect)
			text = font1.render(f"Green: {colors[1]}", True, (255,255,255))
			textRect = text.get_rect()
			textRect.center = (1150,220)
			win.blit(text,textRect)
			text = font1.render(f"Blue: {colors[2]}", True, (255,255,255))
			textRect = text.get_rect()
			textRect.center = (1150,330)
			win.blit(text,textRect)
			text = font1.render(f"({colors[0]},{colors[1]},{colors[2]})", True, (255,255,255))
			textRect = text.get_rect()
			textRect.center = (1150,440)
			win.blit(text,textRect)
			hex_string = '#{:02x}{:02x}{:02x}'.format(colors[0],colors[1],colors[2])
			text = font1.render(f"{hex_string}", True, (255,255,255))
			textRect = text.get_rect()
			textRect.center = (1150,470)
			win.blit(text,textRect)


	else:
		textRect = text.get_rect()
		textRect.center = (600,350)
		win.blit(text,textRect)
	pygame.display.update()








