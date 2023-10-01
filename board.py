import pygame
from settings import *

class Board:
	def draw(self, screen):
		for row in range(BOARD_SIZE):
			for col in range(BOARD_SIZE):
				color = LIGHT_BROWN if (row + col) % 2 == 0 else DARK_BROWN
				pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

	def piece_at_position(self, x, y, all_pieces):
		for piece in all_pieces:
			if piece.x == x and piece.y == y:
				return piece
		return None
