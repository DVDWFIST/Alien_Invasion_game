import pygame

class Ship():
    """Класс для управления кораблем"""
    def __init__(self, screen):
        """Инициализируем корабль и задаем его начальную позицию."""
        self.screen = screen

        #Загружаем изображение корабля и получает прямоугольник.
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #Каждый новый корабль появиться у нижнего края экрана.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Рисуем корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)