import pygame 
from Frontend.constants import WIDTH , HEIGHT 
from Frontend.plateau import Plateau


FPS = 60


WIN = pygame.display.set_mode((WIDTH , HEIGHT))

def main():
    run = True 
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        plateau = Plateau()
        for event in  pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN :
                pos = pygame.mouse.get_pos()
                # row , col = get_row_col_from_mouse(pos)
        
        plateau.draw_squares(WIN)
        pygame.display.update()

    pygame.quit()

main()