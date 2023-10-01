import pygame

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
BOARD_SIZE = 8
SQUARE_SIZE = SCREEN_WIDTH // BOARD_SIZE
SPRITE_SHEET_PATH = 'chess_pieces.png'
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BROWN = (233, 174, 95)
DARK_BROWN = (177, 113, 24)

sprite_sheet = pygame.image.load(SPRITE_SHEET_PATH)
sheet_width, sheet_height = sprite_sheet.get_size()
PIECE_WIDTH = sheet_width // 6
PIECE_HEIGHT = sheet_height // 2



def load_pieces(sprite_sheet):
    pieces_dict = {}
    labels = ['king', 'queen', 'bishop', 'knight', 'rook', 'pawn']

    for i, label in enumerate(labels):
        pieces_dict[f"white_{label}"] = sprite_sheet.subsurface(i * PIECE_WIDTH, 0, PIECE_WIDTH, PIECE_HEIGHT)
        pieces_dict[f"black_{label}"] = sprite_sheet.subsurface(i * PIECE_WIDTH, PIECE_HEIGHT, PIECE_WIDTH, PIECE_HEIGHT)

    return pieces_dict

def update_selected_piece(pieces, selected_piece, available_moves=[]):
	mouseX, mouseY = pygame.mouse.get_pos()
	col = mouseX // SQUARE_SIZE
	row = mouseY // SQUARE_SIZE
	if selected_piece is None:
		for piece in pieces:
			if piece.x == col and piece.y == row:
				selected_piece = piece
				available_moves = selected_piece.valid_moves(pieces)
				original_pos = (piece.x, piece.y)  # Store original position for resetting
				dragging = True  # Start dragging
				break
				
	else:
				selected_piece = None
				available_moves.clear()

	return (selected_piece, available_moves)



pieces_data = load_pieces(sprite_sheet)

pieces_layout = [
    ('rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook'),
    ('pawn',) * 8,
    (),
    (),
    (),
    (),
    ('pawn',) * 8,
    ('rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook')
]

