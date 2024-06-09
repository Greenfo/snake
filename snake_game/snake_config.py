
class Snake:
	def __init__(self,game):
		self.x = 0
		self.y = 0
		self.xspeed = 1
		self.yspeed = 0
		self.scl = 10	
		self.tail = [game.Rect(self.x,self.y, self.scl,self.scl)]	
		self.Snake_rect = game.Rect(self.x+self.scl,self.y, self.scl,self.scl) 
		self.game_over = False
		self.score = 0
		self.text_font = game.font.Font("freesansbold.ttf", 20)

	def death(self,game):
		for i in self.tail:
			if self.Snake_rect.x == i.x and self.Snake_rect.y == i.y:
				self.game_over = True

		if self.game_over:
			self.x = 0
			self.y = 0
			self.xspeed = 1
			self.yspeed = 0
			self.scl = 10	
			self.tail = [game.Rect(self.x,self.y, self.scl,self.scl)]	
			self.Snake_rect = game.Rect(self.x+self.scl,self.y, self.scl,self.scl) 
			self.game_over = False
			self.score = 0
	
	def text(self, screen):
		score1_text = self.text_font.render(f'{self.score}',False, (255,255,255))
		screen.blit(score1_text, (5,0))

	def update(self,width,height,game):

		self.tail.append(self.Snake_rect)
		for i in range(len(self.tail)-1):
			self.tail[i].x ,self.tail[i].y = self.tail[i+1].x ,self.tail[i+1].y
		self.Snake_rect.x += self.xspeed*self.scl
		self.Snake_rect.y += self.yspeed*self.scl
		self.tail.remove(self.Snake_rect)

		if self.Snake_rect.x > width:
			self.Snake_rect.x = 0
		if self.Snake_rect.y > height:
			self.Snake_rect.y = 0
		elif self.Snake_rect.x < 0:
			self.Snake_rect.x = width-10
		elif self.Snake_rect.y < 0:
			self.Snake_rect.y = height-10

	def KeqboardInput(self,game):
		keys=game.key.get_pressed()
		if keys[game.K_UP]:
			self.xspeed = 0
			self.yspeed = -1
		elif keys[game.K_DOWN]:
			self.xspeed = 0
			self.yspeed = 1
		elif keys[game.K_RIGHT]:
			self.xspeed = 1
			self.yspeed = 0
		elif keys[game.K_LEFT]:
			self.xspeed = -1
			self.yspeed = 0