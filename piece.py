import pygame
from settings import *




class Piece:
	def __init__(self, image, x, y, piece_type, color):
		self.image = image
		self.x = x
		self.y = y
		self.piece_type = piece_type  # This will store the type of the piece (e.g., 'king', 'pawn', etc.)
		self.color = color  # This will store the color of the piece ('white' or 'black')
	
		scaled_width = int(SQUARE_SIZE * 1)
		scaled_height = int((scaled_width / PIECE_WIDTH) * PIECE_HEIGHT)
		self.image = pygame.transform.scale(self.image, (scaled_width, scaled_height))
	
	def draw(self, screen):
		offsetX = (SQUARE_SIZE - self.image.get_width()) // 2
		offsetY = (SQUARE_SIZE - self.image.get_height()) // 2
		screen.blit(self.image, (self.x * SQUARE_SIZE + offsetX, self.y * SQUARE_SIZE + offsetY))
	

	
	def valid_moves(self, all_pieces, board):
		moves = []
		
		if self.piece_type == "pawn":
			if self.color == "white":
				# Standard move
				if not board.piece_at_position(self.x, self.y - 1, all_pieces):
					moves.append((self.x, self.y - 1))
					# Check for the initial double move
					if self.y == 6 and not board.piece_at_position(self.x, self.y - 2, all_pieces):
						moves.append((self.x, self.y - 2))
			
				# Capture moves
				if board.piece_at_position(self.x - 1, self.y - 1, all_pieces) and board.piece_at_position(self.x - 1, self.y - 1, all_pieces).color == "black":
					moves.append((self.x - 1, self.y - 1))
				if board.piece_at_position(self.x + 1, self.y - 1, all_pieces) and board.piece_at_position(self.x + 1, self.y - 1, all_pieces).color == "black":
					moves.append((self.x + 1, self.y - 1))
				
			else:
				# Standard move
				if not board.piece_at_position(self.x, self.y + 1, all_pieces):
					moves.append((self.x, self.y + 1))
					# Check for the initial double move
					if self.y == 1 and not board.piece_at_position(self.x, self.y + 2, all_pieces):
						moves.append((self.x, self.y + 2))
				
				# Capture moves
				if board.piece_at_position(self.x - 1, self.y + 1, all_pieces) and board.piece_at_position(self.x - 1, self.y + 1, all_pieces).color == "white":
					moves.append((self.x - 1, self.y + 1))
				if board.piece_at_position(self.x + 1, self.y + 1, all_pieces) and board.piece_at_position(self.x + 1, self.y + 1, all_pieces).color == "white":
					moves.append((self.x + 1, self.y + 1))
		
		elif self.piece_type == "rook":
			for i in range(1, 8):
				moves.append((self.x + i, self.y))
				moves.append((self.x - i, self.y))
				moves.append((self.x, self.y + i))
				moves.append((self.x, self.y - i))
		
		elif self.piece_type == "knight":
			moves.extend([(self.x + 2, self.y + 1), (self.x + 2, self.y - 1), (self.x - 2, self.y + 1), (self.x - 2, self.y - 1),
						  (self.x + 1, self.y + 2), (self.x + 1, self.y - 2), (self.x - 1, self.y + 2), (self.x - 1, self.y - 2)])
		
		elif self.piece_type == "bishop":
			for i in range(1, 8):
				moves.append((self.x + i, self.y + i))
				moves.append((self.x + i, self.y - i))
				moves.append((self.x - i, self.y + i))
				moves.append((self.x - i, self.y - i))
		
		elif self.piece_type == "queen":
			# Combining rook and bishop movements
			for i in range(1, 8):
				moves.append((self.x + i, self.y))
				moves.append((self.x - i, self.y))
				moves.append((self.x, self.y + i))
				moves.append((self.x, self.y - i))
				moves.append((self.x + i, self.y + i))
				moves.append((self.x + i, self.y - i))
				moves.append((self.x - i, self.y + i))
				moves.append((self.x - i, self.y - i))
		
		elif self.piece_type == "king":
			moves.extend([(self.x + 1, self.y), (self.x - 1, self.y), (self.x, self.y + 1), (self.x, self.y - 1),
						  (self.x + 1, self.y + 1), (self.x + 1, self.y - 1), (self.x - 1, self.y + 1), (self.x - 1, self.y - 1)])
		

		valid_moves = []
		for x, y in moves:
			target_piece = board.piece_at_position(x, y, all_pieces)
			
			# If the target position has a piece of the same color, skip this move.
			if target_piece and target_piece.color == self.color:
				continue
			
			if self.piece_type == 'pawn':
				# If there's a piece directly in front of the pawn, skip this move.
				if target_piece and (x - self.x) == 0:
					continue
				# If the pawn moves diagonally, it must be capturing an opponent piece.
				if abs(x - self.x) == 1 and not target_piece:
					continue
			# elif self.piece_type in ['rook', 'bishop', 'queen']:
			# 	if self.is_path_blocked(x, y, all_pieces):  # You need to implement this function.
			# 		continue
			valid_moves.append((x, y))
		
		return valid_moves
