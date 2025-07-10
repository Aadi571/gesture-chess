import pygame
import cv2
import mediapipe as mp
import chess
import chess.engine

# ==========================
# Pygame Setup
# ==========================

WIDTH, HEIGHT = 640, 640
SQUARE_SIZE = WIDTH // 8

pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gesture Chess")

# Load images for pieces (use your own .png files!)
# Example: assets/wP.png, bK.png, etc.
pieces = {}
piece_types = ['P', 'R', 'N', 'B', 'Q', 'K']
colors = ['w', 'b']
for color in colors:
    for piece in piece_types:
        img = pygame.image.load(f'assets/{color}{piece}.png')
        img = pygame.transform.scale(img, (SQUARE_SIZE, SQUARE_SIZE))
        pieces[f'{color}{piece}'] = img

# ==========================
# Chess Setup
# ==========================

board = chess.Board()

# ==========================
# OpenCV + MediaPipe Setup
# ==========================

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5)
mp_draw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

# ==========================
# Functions
# ==========================

def draw_board(win):
    colors = [pygame.Color("white"), pygame.Color("gray")]
    for r in range(8):
        for c in range(8):
            color = colors[(r + c) % 2]
            rect = pygame.Rect(c * SQUARE_SIZE, r * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            pygame.draw.rect(win, color, rect)

def draw_pieces(win, board):
    board_str = str(board)
    rows = board_str.split('\n')
    for r in range(8):
        for c in range(8):
            char = rows[r][c]
            if char == '.':
                continue
            color = 'w' if char.isupper() else 'b'
            piece = char.upper()
            img = pieces[f'{color}{piece}']
            win.blit(img, (c * SQUARE_SIZE, r * SQUARE_SIZE))

def map_hand_to_square(x, y, frame_width, frame_height):
    board_x = int((x / frame_width) * 8)
    board_y = int((y / frame_height) * 8)
    return board_x, board_y

# ==========================
# Main Loop
# ==========================

running = True
selected_square = None

while running:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    finger_x, finger_y = None, None

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)
            lm = handLms.landmark[8]  # Index finger tip
            finger_x = int(lm.x * frame.shape[1])
            finger_y = int(lm.y * frame.shape[0])

            cv2.circle(frame, (finger_x, finger_y), 10, (0, 255, 0), cv2.FILLED)

    cv2.imshow("Hand Tracking", frame)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_board(WIN)
    draw_pieces(WIN, board)

    if finger_x and finger_y:
        bx, by = map_hand_to_square(finger_x, finger_y, frame.shape[1], frame.shape[0])
        if 0 <= bx < 8 and 0 <= by < 8:
            rect = pygame.Rect(bx * SQUARE_SIZE, by * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            pygame.draw.rect(WIN, pygame.Color('red'), rect, 3)

    pygame.display.flip()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

pygame.quit()
cap.release()
cv2.destroyAllWindows()
