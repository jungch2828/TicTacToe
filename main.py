import pygame

pygame.init()
pygame.display.set_caption("TicTacToe")

#screen
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

#board
board = \
[[None, None, None],
 [None, None, None],
 [None, None, None]]

#color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

#game over message font
font = pygame.font.SysFont("", 100)

#etc
clock = pygame.time.Clock()
running = True
line_width = 5
turn = 0

#functions
def grid():
    for i in range(2):
        pygame.draw.line(screen, WHITE, ((screen_width/3)*(i+1), 0), ((screen_width/3)*(i+1), screen_height), line_width)
        pygame.draw.line(screen, WHITE, (0, (screen_height/3)*(i+1)), (screen_width, (screen_height/3)*(i+1)), line_width)

def mouse_check():
    if board[mouse_row][mouse_col] == None:
        return True
    else:
        return False

def mouse_event():
    if 'OX'[turn%2] == 'X':
        if board[mouse_row][mouse_col] == None:
            board[mouse_row][mouse_col] = 'X'
    else:
        if board[mouse_row][mouse_col] == None:
            board[mouse_row][mouse_col] = 'O'

def draw_OX():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 'X':
                X_start_pos = ((row*screen_width/3)+screen_width/12, (col*screen_height/3)+screen_height/12)
                X_end_pos = ((row*screen_width/3)+3*screen_width/12, (col*screen_height/3)+3*screen_height/12)
                pygame.draw.line(screen, WHITE, X_start_pos, X_end_pos, line_width)
                X_start_pos = ((row*screen_width/3)+3*screen_width/12, (col*screen_height/3)+screen_height/12)
                X_end_pos = ((row*screen_width/3)+screen_width/12, (col*screen_height/3)+3*screen_height/12)
                pygame.draw.line(screen, WHITE, X_start_pos, X_end_pos, line_width)
            elif board[row][col] == 'O':
                O_center = ((row*screen_width/3)+screen_width/6, (col*screen_height/3)+screen_height/6)
                pygame.draw.circle(screen, WHITE, O_center, screen_width/12, line_width)

def check_board():
    global var
    if board[1][1] != None:
        var = board[1][1]
        for i in range(3):
            if board[0][i] == board[2][2-i] == var:
                return 1
        if board[1][0] == board[1][2] == var:
            return 1
    if board[0][0] != None:
        var = board[0][0]
        if board[0][1] == board[0][2] == var or board[1][0] == board[2][0] == var:
            return 1
    if board[2][2] != None:
        var = board[2][2]
        if board[2][0] == board[2][1] == var or board[0][2] == board[1][2] == var:
            return 1
    if turn >= 9:
            return 2

def check_game_over():
    if check_board():
        if check_board() == 1:
            message = font.render(f'{var} WON!', True, WHITE)
        elif check_board() == 2:
            message = font.render('TIE!', True, WHITE)
        message_rect = message.get_rect()
        message_rect.center = (screen_width/2, screen_height/2)
        pygame.draw.rect(screen, BLACK, message_rect)
        screen.blit(message, message_rect)
        pygame.display.update()
        pygame.time.wait(1000)
        pygame.exit()

while running:
    check_game_over()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(board)
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mouse_check():
                turn += 1
                mouse_event()

    mouse_x = pygame.mouse.get_pos()[0]
    mouse_y = pygame.mouse.get_pos()[1]
    mouse_row = int(mouse_x//(screen_width/3))
    mouse_col = int(mouse_y//(screen_height/3))

    draw_OX()
    grid()

    pygame.display.flip()
pygame.quit()