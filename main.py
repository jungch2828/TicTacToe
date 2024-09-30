import pygame

pygame.init()
pygame.display.set_caption("TicTacToe")

SCREEN_SIZE = 600
SQUARE_SIZE = SCREEN_SIZE / 3
LINE_WIDTH = 10
SCREEN = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

FONT = pygame.font.SysFont("", 100)

CLOCK = pygame.time.Clock()
FPS = 60

board = \
[[None, None, None],
 [None, None, None],
 [None, None, None]]

turn = 0
gaming = True
result = ""

def draw_grid():
    for i in range(1, 3):
        pygame.draw.line(SCREEN, WHITE, ((i * SQUARE_SIZE), 0), ((i * SCREEN_SIZE/3), SCREEN_SIZE), LINE_WIDTH)
        pygame.draw.line(SCREEN, WHITE, (0, (i * SQUARE_SIZE)), (SCREEN_SIZE, (i * SQUARE_SIZE)), LINE_WIDTH)

def draw_board():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 'X': 
                draw_x(row, col)
            elif board[row][col] == 'O': 
                draw_o(row, col)

def draw_x(row, col):
    start = ((row * SQUARE_SIZE) + SCREEN_SIZE / 12, (col * SQUARE_SIZE) + SCREEN_SIZE / 12)
    end = ((row * SQUARE_SIZE) + 3 * SCREEN_SIZE / 12, (col * SQUARE_SIZE) + 3 * SCREEN_SIZE / 12)
    pygame.draw.line(SCREEN, WHITE, start, end, LINE_WIDTH)

    start = ((row * SQUARE_SIZE) + 3 * SCREEN_SIZE / 12, (col * SQUARE_SIZE) + SCREEN_SIZE / 12)
    end = ((row * SQUARE_SIZE) + SCREEN_SIZE / 12, (col * SQUARE_SIZE) + 3 * SCREEN_SIZE / 12)
    pygame.draw.line(SCREEN, WHITE, start, end, LINE_WIDTH)

def draw_o(row, col):
    center = ((row * SQUARE_SIZE) + SCREEN_SIZE / 6, (col * SQUARE_SIZE) + SCREEN_SIZE / 6)
    pygame.draw.circle(SCREEN, WHITE, center, SCREEN_SIZE / 12, LINE_WIDTH)

def mouse_event():
    if 'OX'[turn % 2] == 'X': 
        board[mouse_row][mouse_col] = 'X'
    else: 
        board[mouse_row][mouse_col] = 'O'

def check_result():
    global gaming
    global result

    if board[1][1] != None:
        var = board[1][1]
        for i in range(3):
            if board[0][i] == board[2][2-i] == var:
                gaming = False
                result = "o_won" if (var == "O") else "x_won"
        if board[1][0] == board[1][2] == var:
            gaming = False
            result = "o_won" if (var == "O") else "x_won"
    if board[0][0] != None:
        var = board[0][0]
        if board[0][1] == board[0][2] == var or board[1][0] == board[2][0] == var:
            gaming = False
            result = "o_won" if (var == "O") else "x_won"
    if board[2][2] != None:
        var = board[2][2]
        if board[2][0] == board[2][1] == var or board[0][2] == board[1][2] == var:
            gaming = False
            result = "o_won" if (var == "O") else "x_won"

    if result == "" and turn >= 9:
            gaming = False
            result = "tie"

def show_result():
    if result == "o_won":
        message = FONT.render('O WON!', True, WHITE)
    elif result == "x_won":
        message = FONT.render('X WON!', True, WHITE)
    elif result == "tie":
        message = FONT.render('TIE!', True, WHITE)

    message_rect = message.get_rect()
    message_rect.center = (SCREEN_SIZE/2, SCREEN_SIZE/2)
    pygame.draw.rect(SCREEN, BLACK, message_rect)
    SCREEN.blit(message, message_rect)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if gaming and board[mouse_row][mouse_col] == None:
                turn += 1
                mouse_event()

    mouse_x = pygame.mouse.get_pos()[0]
    mouse_y = pygame.mouse.get_pos()[1]
    mouse_row = int(mouse_x//SQUARE_SIZE)
    mouse_col = int(mouse_y//SQUARE_SIZE)

    draw_grid()
    draw_board()

    check_result()

    if(not gaming):
        show_result()

    pygame.display.flip()
    CLOCK.tick(FPS)
