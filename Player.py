from ctypes import util
from turtle import screensize
import pygame
import utils
import random
import colors

class Snail(pygame.sprite.Sprite):
    def __init__(self, params: dict) -> None:
        super().__init__()
        self.image = pygame.image.load("./media/snail.png")
        self.rect = pygame.Rect(10.0, 10.0, 592.0, 592.0)
        # self.rect.center = (320, 180)
        self.params = params

    def update(self) -> None:
        pressed_keys = pygame.key.get_pressed()

        if self.rect.left > 0 and pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-self.params["VEL_NORMAL"], 0)
        if self.rect.right < self.params["SCREEN_WIDTH"] and pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(self.params["VEL_NORMAL"], 0)
        if self.rect.top > 0 and pressed_keys[pygame.K_UP]:
            self.rect.move_ip(0, -self.params["VEL_NORMAL"])
        if self.rect.bottom < self.params["SCREEN_HEIGHT"] and pressed_keys[pygame.K_DOWN]:
            self.rect.move_ip(0, self.params["VEL_NORMAL"])
    
    def draw(self, screen: pygame.Surface) -> None:
        assert type(screen)==pygame.Surface
        screen.blit(self.image, self.rect)

class Bear(pygame.sprite.Sprite):
    def __init__(self, params: dict) -> None:
        super().__init__()
        self.image = pygame.image.load("./media/bear.png")
        self.rect = pygame.Rect(320.0, 180.0, 216.0, 233.0)
        # self.rect.center = (640, 360)
        self.params = params
    
    def move(self) -> None:
        self.rect.move_ip(0, self.params["VEL_FAST"])
        if (self.rect.bottom > 1080):
            self.rect.center = (640, 0)
    
    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.image, self.rect)
        if self.params["DRAW_RECT"]:
            pygame.draw.rect(screen, colors.RED, self.rect, self.rect.width)