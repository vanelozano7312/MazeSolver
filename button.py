from turtle import position
import pygame

#button class
class Button():
    
	def __init__(self, size, position, image):
        #cargar imagenes y escalarlas
		self.position = position
		self.button_view = pygame.image.load(f'static/images/botones/{image}.png')
		self.button_view = pygame.transform.scale(self.button_view, size)
		self.rect = self.button_view.get_rect()
		self.rect.topleft = position
		self.clicked = False

	def pressed(self, size, image_pressed):
		self.button_pressed_view = pygame.image.load(f'static/images/botones/{image_pressed}.png')
		self.button_pressed_view = pygame.transform.scale(self.button_pressed_view, size)

	def button_pressed(self, event):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if event.type == pygame.MOUSEBUTTONDOWN and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False
		
		pressed = action
		return action

     
	def draw(self, surface):
		#draw button on screen
		surface.blit(self.button_view, self.position)
  
	def draw_pressed(self, surface, pressed):
		if pressed:
			#draw button on screen
			surface.blit(self.button_pressed_view, self.position)
		else:
			#draw button on screen
			surface.blit(self.button_view, self.position)
      