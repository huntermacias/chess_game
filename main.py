import pygame
import sys

# local import
from piece import Piece
from board import Board
from settings import *

# Initialize pygame
pygame.init()

# setup pieces
pieces = []
for row, layout_row in enumerate(pieces_layout):
    for col, piece in enumerate(layout_row):
        color = 'white' if row > 4 else 'black'
        pieces.append(Piece(pieces_data[f"{color}_{piece}"], col, row, piece, color))


# Setup display and clock
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Chess')
clock = pygame.time.Clock()


def main():
	board = Board()
	
	selected_piece = None
	available_moves = []
	dragging = False
	original_pos = None
	original_mouse_pos = None  # Added to get offset for dragging
    
	# Game Loop
	while True:
		
		# Event Loop
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouseX, mouseY = pygame.mouse.get_pos()
				col = mouseX // SQUARE_SIZE
				row = mouseY // SQUARE_SIZE
				if selected_piece is None:
					for piece in pieces:
						if piece.x == col and piece.y == row:
							selected_piece = piece
							available_moves = selected_piece.valid_moves(pieces, board)
							original_pos = (piece.x, piece.y)
							original_mouse_pos = (mouseX, mouseY)
							dragging = True  # Start dragging
							break
		
			elif event.type == pygame.MOUSEBUTTONUP and dragging:
				mouseX, mouseY = pygame.mouse.get_pos()
				col = mouseX // SQUARE_SIZE
				row = mouseY // SQUARE_SIZE
				captured_piece = board.piece_at_position(col, row, pieces)  # Check if there's a piece at the target position
				if (col, row) in available_moves:
					selected_piece.x = col
					selected_piece.y = row
					if captured_piece:
						pieces.remove(captured_piece)  # Remove the captured piece from the list
					else:
						selected_piece.x, selected_piece.y = original_pos  # Reset to the original position
						dragging = False
						selected_piece = None
						available_moves.clear()

				elif dragging:
					mouseX, mouseY = pygame.mouse.get_pos()
					offsetX = mouseX - original_mouse_pos[0]
					offsetY = mouseY - original_mouse_pos[1]
					selected_piece.x = (original_pos[0] * SQUARE_SIZE + offsetX) // SQUARE_SIZE
					selected_piece.y = (original_pos[1] * SQUARE_SIZE + offsetY) // SQUARE_SIZE

		board.draw(screen)
		for piece in pieces:
			piece.draw(screen)
		
		for move in available_moves:
			pygame.draw.circle(screen, (97, 70, 170, 1), (move[0]*SQUARE_SIZE + SQUARE_SIZE//2, move[1]*SQUARE_SIZE + SQUARE_SIZE//2), 12)
		
		pygame.display.flip()
		clock.tick(60)





if __name__ == "__main__":
    main()
