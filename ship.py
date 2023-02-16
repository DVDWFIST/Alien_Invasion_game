import pygame


class Ship():
    """Класс для управления кораблем"""

    def __init__ (self, ai_settings, screen):
        """Инициализируем корабль и задаем его начальную позицию."""
        self.screen = screen
        self.ai_settings = ai_settings

        # Загружаем изображение корабля и получает прямоугольник.
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Каждый новый корабль появиться у нижнего края экрана.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Сохраняем вещественной координатой центр корабля.
        self.center = float(self.rect.centerx)

        # Флаг перемещения.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Обновляет позицию корабля с учетом флага."""

        # Обновляем атрибуты center, не rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # Обновляем атрибуты rect на основе self.center.
        self.rect.centerx = self.center

    def blitme(self):
        """Рисуем корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)
