from operator import truediv
from numpy import blackman, place
import pygame
import sys
import colors
from Player import Bear, Snail

# define all global variables here
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

FPS = 60

PARAMS = {
    "VEL_NORMAL":       5.0,
    "VEL_FAST"  :       10.0,
    "VEL_SLOW"  :       2.5,
    "SCREEN_WIDTH" :    1920,
    "SCREEN_HEIGHT" :   1080,
    "DRAW_RECT":        False
}

def main():
    pygame.init()

    if pygame.get_init():
        print("\033[1;32mPygame is correctly initialized.\033[0m")
        
    frame_per_sec = pygame.time.Clock()

    logo = pygame.image.load("./media/logo.png")

    pygame.display.set_icon(logo)

    pygame.display.set_caption("Pygame Tutorials")

    screen = pygame.display.set_mode((PARAMS["SCREEN_WIDTH"], PARAMS["SCREEN_HEIGHT"]))
    screen.fill(colors.WHITE)
    print(type(screen))

    running = True

    draw_point = [320, 180]

    snail = Snail(params=PARAMS)

    bear = Bear(params=PARAMS)

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
                
                # For debugging
                if event.key == pygame.K_p:
                    print("Printing debugging info...")
                    print(f"The snail coordinates are:   ({snail.rect.left: .2f}, {snail.rect.top: .2f}")
                    print(f"The bear  coordinates are:   ({snail.rect.left: .2f}, {snail.rect.top: .2f}")


            # Keyup
            if event.type == pygame.KEYUP:
                print("Key released.")
                if event.key == pygame.K_SPACE:
                    print("Space bar released.")

        # update all characters
        snail.update()
        bear.move()

        # draw everything to the screen
        screen.fill(colors.WHITE)
        bear.draw(screen)
        snail.draw(screen)

        # push the image to display
        pygame.display.update()
        frame_per_sec.tick(FPS)

if __name__=="__main__":
    main()
