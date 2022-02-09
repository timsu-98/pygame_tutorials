from numpy import blackman, place
import pygame
import sys
import colors
from Player import Snail

def main():
    pygame.init()

    if pygame.get_init():
        print("\033[1;32mPygame is correctly initialized.\033[0m")

    FPS = 60
    frame_per_sec = pygame.time.Clock()

    logo = pygame.image.load("./media/logo.png")

    pygame.display.set_icon(logo)

    pygame.display.set_caption("Pygame Tutorials")

    screen = pygame.display.set_mode((640, 360))
    screen.fill(colors.WHITE)
    print(type(screen))

    running = True

    draw_point = [320, 180]

    snail = Snail()


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
        snail.update()
        snail.draw(screen)

        pygame.display.update()
        frame_per_sec.tick(FPS)

        
    

if __name__=="__main__":
    main()
