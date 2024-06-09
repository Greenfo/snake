import pygame

from snake_config import Snake
from apple_config import Apple

pygame.init()

width = 500
height = 500

def main():
	screen = pygame.display.set_mode((width,height))
	text_font = pygame.font.Font("freesansbold.ttf", 20)
	run = True
	clock = pygame.time.Clock()
	s = Snake(pygame)
	a = Apple(pygame,width,height) 
	while run:
		clock.tick(10)
		screen.fill((0,0,0))
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		s.death(pygame)
		s.KeqboardInput(pygame)
		s.update(width,height,pygame)
		a.draw(pygame,screen)
		s.text(screen)

		for square in s.tail:
			pygame.draw.rect(screen, (255,255,255), square)
		pygame.draw.rect(screen, (255,255,255), s.Snake_rect)

		if s.Snake_rect.colliderect(a.apple_rect):
			s.tail.append(pygame.Rect(square.x,square.y,s.scl,s.scl))
			a.picklocation(width,height)
			s.score += 1 


		pygame.display.update()
if __name__=="__main__":
	main()