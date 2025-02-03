from config import *
import random
import pygame


class Ball:
    def __init__(self):
        self.radius = BALL_RADIUS
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.dx = random.choice([-1, 1]) * BALL_SPEED
        self.dy = -BALL_SPEED
        self.rect = pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)

    def move(self):
        """Движение мяча"""
        self.x += self.dx
        self.y += self.dy
        self.rect.x = self.x - self.radius
        self.rect.y = self.y - self.radius

        # Отражение от стен
        if self.x - self.radius <= 0 or self.x + self.radius >= WIDTH:
            self.dx *= -1
        if self.y - self.radius <= 0:
            self.dy *= -1

    def draw(self):
        """Отрисовка мяча"""
        pygame.draw.circle(screen, RED, (int(self.x), int(self.y)), self.radius)

    def check_collision_with_paddle(self, paddle):
        """Проверка столкновения с платформой"""
        if paddle.rect.colliderect(self.rect):
            self.dy *= -1

    def check_collision_with_bricks(self, bricks):
        """Проверка столкновения с кирпичами"""
        for brick in bricks[:]:
            if self.rect.colliderect(brick.rect):
                if brick.hit():
                    bricks.remove(brick)
                self.dy *= -1
                return True
        return False
