import pygame

ROWS = COLS = 15
map = [0]*ROWS
for i in range(ROWS):
    map[i] = [0]*COLS

EMPTY = 0
BLACK = 1
WHITE = 2
last = BLACK # the first player is WHITE

pygame.init()
screen = pygame.display.set_mode((750,750))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            col = round((x-25)/50)
            row = round((y-25)/50)
            print(col+1,row+1)
            if map[row][col] == EMPTY and last == BLACK:
                map[row][col] = WHITE
                last = WHITE
            elif map[row][col] == EMPTY and last == WHITE:
                map[row][col] = BLACK
                last = BLACK
            else:
                print("Already filled")

    screen.fill("#EE9A49")

    for x in range(COLS):
        pygame.draw.line(screen, "#000000", [25+x*50, 25], [25+x*50, 725], 2) 
    for y in range(ROWS):
        pygame.draw.line(screen, "#000000", [25, 25+y*50], [725, 25+y*50], 2)
    
    pygame.draw.circle(screen, "#000000", [25+7*50, 25+7*50], 8)

    x,y = pygame.mouse.get_pos()
    x = round((x-25)/50)*50+25
    y = round((y-25)/50)*50+25

    pygame.draw.rect(screen, "#FFFFFF", [x-25, y-25, 50, 50], 2)

    for row in range(ROWS):
        for col in range(COLS):
            if map[row][col] == BLACK:
                pygame.draw.circle(screen, "#000000", [25+col*50, 25+row*50], 25)
            elif map[row][col] == WHITE:
                pygame.draw.circle(screen, "#FFFFFF", [25+col*50, 25+row*50], 25)

    pygame.display.update()

pygame.quit()