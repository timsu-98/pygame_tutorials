import pygame
import utils

class Snail(pygame.sprite.Sprite):
    def __init__(self, orientation = utils.UP) -> None:
        super().__init__()
        self.image = pygame.image.load("./media/snail.png")
        self.rect = pygame.Rect(320, 180, 30, 30)
        self.rect.center = (320, 180)
        self.orientation = orientation

    def update(self) -> None:
        pressed_keys = pygame.key.get_pressed()

        if self.rect.left > 0:
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-10, 0)
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(10, 0)
    
    def draw(self, screen: pygame.Surface) -> None:
        assert type(screen)==pygame.Surface
        screen.blit(self.image, self.rect)

        
