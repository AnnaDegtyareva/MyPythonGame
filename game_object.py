import pygame
from constants import *

img0 = 'boy.png'
img1 = 'boy1.png'
img2 = 'boy5.png'

class Player(pygame.sprite.Sprite):
    """ Этот класс описывает управление и поведение спрайта игрока
    """
    # Конструктор класса
    def __init__(self, x, y, img = img0):
        super().__init__()

        # Загружаем изображение спрайта
        self.image = pygame.image.load(img).convert_alpha()
        # Задаем положение спрайта игрока на экране
        self.rect = self.image.get_rect()
        
        self.rect.x = x
        self.rect.y = y
        
        # Задаем скорость игрока по x и по y
        self.change_x = 0
        self.change_y = 0

        self.floors = pygame.sprite.Group()
        self.artifacts = pygame.sprite.Group()
        self.frends = pygame.sprite.Group()
        
        self.score = 0
        self.lives = 5


    def update(self):
        
        walk_cooldown = 5
        # учитываем эффект гравитации:
        self.calc_grav()
        # Пересчитываем положение спрайта игрока на экране

        # Смещение влево - вправо
        self.rect.x += self.change_x

        # Проверяем столкновение с препятствием
        block_hit_list = pygame.sprite.spritecollide(self, self.floors, False)
        for block in block_hit_list:
            # Если персонаж двигался вправо, остановим его слева от препятствия
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Наоборот, если движение было влево остановим его справа от препятствия
                self.rect.left = block.rect.right

        # Движение вверх-вниз
        self.rect.y += self.change_y

        # Проверяем столкновение с препятствием
        block_hit_list = pygame.sprite.spritecollide(self, self.floors, False)
        for block in block_hit_list:
            # Прид вижении вниз, персонаж упал на препятвие - он должен встать на него сверху
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            # В прыжке персонаж врезался в препятствия - движение вверх должно прекратиться.
            self.change_y = 0
        


    # Расчет гравитации
    def calc_grav(self):
        if self.change_y == 0:
            self.change_y = 1
        else:
            # Моделируем ускорение свободного падения:
            self.change_y += .35

        # Проверка: персонаж на земле или нет
        if self.rect.y >= WIN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = WIN_HEIGHT - self.rect.height

        # Проверка: выход за границу экрана
        if self.rect.x < 0 :
            self.rect.x = 0
            self.change_x = 0
        if self.rect.x > WIN_WIDTH - self.rect.width:
            self.rect.x = WIN_WIDTH - self.rect.width
            self.change_x = 0

    def jump(self):
        """ Called when user hits 'jump' button. """

        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down
        # 1 when working with a platform moving down.
        self.rect.y += 2
        floor_hit_list = pygame.sprite.spritecollide(self, self.floors, False)
        self.rect.y -= 2

        # If it is ok to jump, set our speed upwards
        if len(floor_hit_list) > 0 or self.rect.bottom >= WIN_HEIGHT:
            self.change_y = -10

    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -4
        self.image = pygame.image.load(img2).convert_alpha()

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 4
        self.image = pygame.image.load(img1).convert_alpha()

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0
        self.image = pygame.image.load(img0).convert_alpha()
    



class Grandfather(pygame.sprite.Sprite):
    # Конструктор класса
    def __init__(self, x, y, img = 'grandfather.png'):
        super().__init__()

        # Загружаем изображение спрайта
        self.image = pygame.image.load(img).convert_alpha()
        # Задаем положение спрайта игрока на экране
        self.rect = self.image.get_rect()
        
        self.rect.x = x
        self.rect.y = y

class TimeMachine(pygame.sprite.Sprite):
    # Конструктор класса
    def __init__(self, x, y, img = 'time_machine.png'):
        super().__init__()

        # Загружаем изображение спрайта
        self.image = pygame.image.load(img).convert_alpha()
        # Задаем положение спрайта игрока на экране
        self.rect = self.image.get_rect()
        
        self.rect.x = x
        self.rect.y = y

class Frends1(pygame.sprite.Sprite):
    # Конструктор класса
    def __init__(self, x, y, img = 'T-200.png'):
        super().__init__()

        # Загружаем изображение спрайта
        self.image = pygame.image.load(img).convert_alpha()
        # Задаем положение спрайта игрока на экране
        self.rect = self.image.get_rect()
        
        self.rect.x = x
        self.rect.y = y

class Frends2(pygame.sprite.Sprite):
    # Конструктор класса
    def __init__(self, x, y, img = 'T-300.png'):
        super().__init__()

        # Загружаем изображение спрайта
        self.image = pygame.image.load(img).convert_alpha()
        # Задаем положение спрайта игрока на экране
        self.rect = self.image.get_rect()
        
        self.rect.x = x
        self.rect.y = y


class BB8(pygame.sprite.Sprite):
    # Конструктор класса
    def __init__(self, x, y, img = 'BB-8.png'):
        super().__init__()

        # Загружаем изображение спрайта
        self.image = pygame.image.load(img).convert_alpha()
        # Задаем положение спрайта игрока на экране
        self.rect = self.image.get_rect()
        
        self.rect.x = x
        self.rect.y = y

        
        