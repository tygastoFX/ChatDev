'''
This file contains the Pong class.
'''
import pygame
class Pong:
    def __init__(self, screen, screen_width, screen_height, side):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.side = side
        self.width = 10
        self.height = 60
        self.color = (255, 255, 255)
        self.speed = 5
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.reset_position()
    def reset_position(self):
        if self.side == "left":
            self.rect.x = 20
        elif self.side == "right":
            self.rect.x = self.screen_width - self.width - 20
        self.rect.y = self.screen_height // 2 - self.height // 2
    def update(self):
        if self.side == "left":
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w] and self.rect.y > 0:
                self.rect.y -= self.speed
            if keys[pygame.K_s] and self.rect.y < self.screen_height - self.height:
                self.rect.y += self.speed
        elif self.side == "right":
            if self.rect.y < self.screen_height // 2 and self.rect.y > 0:
                self.rect.y -= self.speed
            elif self.rect.y > self.screen_height // 2 and self.rect.y < self.screen_height - self.height:
                self.rect.y += self.speed
            else:
                self.rect.y += random.choice([-1, 1]) * self.speed
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)