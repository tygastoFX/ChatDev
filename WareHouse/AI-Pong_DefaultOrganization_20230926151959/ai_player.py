'''
This file contains the AIPlayer class.
'''
import pygame
import random
class AIPlayer:
    def __init__(self, pong, screen_height):
        self.pong = pong
        self.screen_height = screen_height
        self.speed = 3
    def update(self):
        if self.pong.rect.y < self.screen_height // 2 and self.pong.rect.y > 0:
            self.pong.rect.y -= self.speed
        elif self.pong.rect.y > self.screen_height // 2 and self.pong.rect.y < self.screen_height - self.pong.height:
            self.pong.rect.y += self.speed
        else:
            self.pong.rect.y += random.choice([-1, 1]) * self.speed