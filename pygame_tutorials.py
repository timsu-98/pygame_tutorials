from turtle import screensize
from numpy import blackman, place
import pygame
import sys
import colors

def main():
    pygame.init()

    if pygame.get_init():
        print("\033[1;32mPygame is correctly initialized.\033[0m")

    logo = pygame.image.load("./media/logo.png")

    pygame.display.set_icon(logo)

    pygame.display.set_caption("Pygame Tutorials")

    screen = pygame.display.set_mode((640, 360))
    screen.fill(colors.WHITE)

    running = True

    draw_point = [320, 180]

    # Game loop
    while running:
        for event in pygame.event.get():
            # The game ended here
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            # Keydown
            if event.type == pygame.KEYDOWN:
                print("Key pressed!")
                if event.key == pygame.K_SPACE:
                    print("Space bar pressed.")
                    pygame.draw.circle(screen, colors.BLUE, draw_point, 5)
                    draw_point[0] += 10
                    draw_point[1] += 10
            # Keyup
            if event.type == pygame.KEYUP:
                print("Key released.")
                if event.key == pygame.K_SPACE:
                    print("Space bar released.")
        pygame.display.update()

        
    

if __name__=="__main__":
    main()
