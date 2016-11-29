import pygame as pg
import sys
from pygame.locals import *
from pygame.sprite import *
from random import *

DISPLAYSURF = pg.display.set_mode((1000, 700))

class MenuItem(pg.font.Font):
	def __init__(self, text, font=None, font_size = 30, font_color=(0,0,255), pos_x = 0, pos_y = 0):
		pg.font.Font.__init__(self, font, font_size)
		self.text = text
		self.font_size = font_size
		self.font_color = font_color
		self.label = self.render(self.text, 1, self.font_color)
		self.width = self.label.get_rect().width
		self.height = self.label.get_rect().height
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.position = pos_x, pos_y

	def set_position(self, x, y):
		self.position = (x,y)
		self.pos_x = x
		self.pos_y = y


	def is_mouse_selection(self, pos):
		lst = list(pos)
		posx = lst[0]
		posy = lst[1]
		if (posx >= self.pos_x and posx <= self.pos_x + self.width) and (posy >= self.pos_y and posy <= self.pos_y + self.height):
			return True
		return False

	def set_font_color(self, rgb_tuple):
		self.font_color = rgb_tuple
		self.label = self.render(self.text, 1, self.font_color)


#Creating a menu
class GameMenu():
	def __init__(self, screen, items, bg_color=black, font = None, font_size = 30, font_color = (0,0,255), pos_x = 0, pos_y = 0):
		self.screen = screen
		self.scr_width = self.screen.get_rect().width
		self.scr_height = self.screen.get_rect().height
		self.bg_color = bg_color
		self.clock = fpsClock
		self.font = pg.font.SysFont(font, font_size)
		self.font_color = font_color
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.position = pos_x, pos_y

		self.items = []

		#
		for index, item in enumerate(items):
			menu_item = MenuItem(item)
			#label = self.font.render(item, 1, font_color)

			# width = label.get_rect().width
			# height = label.get_rect().height

			posx = (self.scr_width/2) - (menu_item.width/2)
			#t_h is abbreviated total height of the text block
			t_h = len(items)*menu_item.height
			#posy is position of y
			posy = (self.scr_height/2)-(t_h/2)+((index*2) + index * menu_item.height)
			menu_item.set_position(pos_x, pos_y)
			self.items.append(menu_item)
			print("click")


	def run(self):
		# mainLoop = True
		while True:
			self.clock.tick(FPS)

			#This will Redraw the background
			self.screen.fill(self.bg_color)

			for item in self.items:
				if item.is_mouse_selection(pg.mouse.get_pos()):
					item.set_font_color((255,0,0))
					item.set_italic(True)
				else:
					item.set_font_color((255, 255, 255))
					item.set_italic(False)
				self.screen.blit(item.label, item.position)

			for event in pg.event.get():
				if event.type == pg.QUIT:
					sys.exit()

			pg.display.flip()

	def set_font_color(self, rgb_tuple):
		self.font_color = rgb_tuple
		self.label = self.render(self.text, 1, self.font_color)

	def set_mouse_selection(self, item, mpos):
		if item.is_mouse_selection(mpos):
			item.set_font_color(red)
			item.set_italic(True)
		else:
			item.set_font_color(white)
			item.set_italic(False)



def main():

	game_over = False

	hand = MasterHand(everything)

	while True:

		menu_items = ('Start', 'Quit')
		gm = GameMenu(DISPLAYSURF, menu_items)
		gm.run()
		

		DISPLAYSURF.fill(black)
		#always do an updated here of hand.handx and hand.handy		

		pg.display.update()
		fpsClock.tick(FPS)

	pg.quit()
