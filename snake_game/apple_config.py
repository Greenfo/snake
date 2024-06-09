from random import randint
class Apple:
	def __init__(self,game,width,height):
		self.scl = 10
		self.x = randint(0,(width-self.scl)/self.scl)
		self.y = randint(0,(height-self.scl)/self.scl)
		self.apple_rect = game.Rect(self.x*self.scl,self.y*self.scl, self.scl,self.scl)

	def picklocation(self,width,height):
		self.x = randint(0,(width-self.scl)/self.scl)
		self.y = randint(0,(height-self.scl)/self.scl)
		self.apple_rect.x = self.x*self.scl
		self.apple_rect.y = self.y*self.scl

	def draw(self, game,screen):
		game.draw.rect(screen, (255,0,0), self.apple_rect)
