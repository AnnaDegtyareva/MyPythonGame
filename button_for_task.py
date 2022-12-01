import pygame
from constants import *

# Класс позволяет создать прямоугольную кнопку с надписью на ней
class Button():
    def __init__(
            self, x, y, w, h, name,
            font_color=WHITE,
            normal_color=PURPULE,
            highlight_color = MINT,
            active_color=BLACK,
            size=24,
            font='Arial',
            padding=5
    ):
        # Текущее состояние кнопки. Все состояния: 'normal', 'highlight', 'active'
        self.state = 'normal'
        # Задаем цвета кнопки в нормальном, веделенном и активном состоянии:
        self.normal_color = normal_color
        self.highlight_color = highlight_color
        self.active_color = active_color
        # Задаем название  - текст на кнопке
        self.name = name
        self.font = pygame.font.SysFont(font, size, True)
        # Создаем надпись на кнопке
        self.text = self.font.render(name, True, font_color)
        # Задаем размеры прямоугольника
        self.image = pygame.Surface([w,h])
        self.image.fill(normal_color)
        # Задаем положение верхней панели на экране
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # Задаем поля - отступы от границы кнопки для текста
        self.padding = padding

    # Рисуем прямоугольник кнопки и надпись на ней
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        screen.blit(self.text, (self.rect.x + self.padding, self.rect.y + self.padding))

    # В методе update меняем цвет кнопки в зависимости от состояния
    def update(self):
        if self.state == 'normal':
            self.image.fill(self.normal_color)
        elif self.state == 'highlight':
            self.image.fill(self.highlight_color)
        elif self.state == 'active':
            self.image.fill(self.active_color)

    # Обработка событий кнопки:  меняем состояние в зависимости от события
    def handle_mouse_action(self, event=None):
        # Получаем текущее положение курсора
        pos_x, pos_y = pygame.mouse.get_pos()
        # Проверяем, находится курсор над кнопкой или нет:
        check_pos = self.rect.left <= pos_x <= self.rect.right and self.rect.top <= pos_y <= self.rect.bottom
        # Курсор движется над кнопкой:
        if event == pygame.MOUSEMOTION:
            if check_pos:  self.state = 'highlight'
            else: self.state = 'normal'

        # На кнопку кликнули:
        elif event == pygame.MOUSEBUTTONDOWN:
            if check_pos: self.state = 'active'
            else: self.state = 'normal'
            
        # На кнопку кликнули и отпустили:
        elif event == pygame.MOUSEBUTTONUP:
            if check_pos:  self.state = 'highlight'
            else: self.state = 'normal'



class ButtonForTask5():
    def __init__(self, w, h):
        # Создаем список пунктов меню:
        self.labels = [
            #'38 ° 15'39″ ю.ш. 175 ° 06'13 ″ в.д.',
            #'с ошибками',
            #'с ошибками',
            'A',
            'B',
            'C',
            
            
        ]
        # Задаем координаты верхнего левого угла меню:
        self.x = 600
        self.y = 360
        # Создаем список кнопок:
        self.buttons5 = []
        # Рассчитываем высоту для каждой кнопки меню, исходя и общей высоты:
        button_height5 = int(h / (len(self.labels) + 1))
        # Локальная переменная, хранит y координату для текущей кнопки:
        current_y = self.y
        for label in self.labels:
            # Создаем новую кнопку:
            new_button = Button(self.x, current_y, w, button_height5, label)
            # Переходим по вертикали к следующей кнопке с отступом в 2 пикселя,
            # чтобы кнопки визуально не "слиплись" между собой:
            current_y += button_height5 + 2
            # Добавляем новую кнопку в список всех кнопок меню:
            self.buttons5.append(new_button)

    # Вызвать метод update() для всех кнопок в меню:
    def update(self):
        for button in self.buttons5:
            button.update()

    # Вызвать метод обработки события для всех кнопок в меню:
    def handle_mouse_event(self, event):
        for button in self.buttons5:
            button.handle_mouse_action(event)
            # запоминаем и возвращаем кнопку, на которую сейчас нажали:
            if button.state == 'active':
                return button

    # Вызвать метод draw для всех кнопок в меню
    def draw(self, screen):
        for button in self.buttons5:
            button.draw(screen)

class ButtonForTask6():
    def __init__(self, w, h):
        # Создаем список пунктов меню:
        self.labels = [
            #'ХNaCl - хлорид натрия',
            #'H2O - вода',
            #'HIO3 - йодноватая кислота',
            'A',
            'B',
            'C',
            
            
        ]
        # Задаем координаты верхнего левого угла меню:
        self.x = 50
        self.y = 300
        # Создаем список кнопок:
        self.buttons6 = []
        # Рассчитываем высоту для каждой кнопки меню, исходя и общей высоты:
        button_height6 = int(h / (len(self.labels) + 1))
        # Локальная переменная, хранит y координату для текущей кнопки:
        current_y = self.y
        for label in self.labels:
            # Создаем новую кнопку:
            new_button = Button(self.x, current_y, w, button_height6, label)
            # Переходим по вертикали к следующей кнопке с отступом в 2 пикселя,
            # чтобы кнопки визуально не "слиплись" между собой:
            current_y += button_height6 + 2
            # Добавляем новую кнопку в список всех кнопок меню:
            self.buttons6.append(new_button)

    # Вызвать метод update() для всех кнопок в меню:
    def update(self):
        for button in self.buttons6:
            button.update()

    # Вызвать метод обработки события для всех кнопок в меню:
    def handle_mouse_event(self, event):
        for button in self.buttons6:
            button.handle_mouse_action(event)
            # запоминаем и возвращаем кнопку, на которую сейчас нажали:
            if button.state == 'active':
                return button

    # Вызвать метод draw для всех кнопок в меню
    def draw(self, screen):
        for button in self.buttons6:
            button.draw(screen)

class ButtonForTask1():
    def __init__(self, w, h):
        # Создаем список пунктов меню:
        self.labels = [
            #'Хищнечество',
            #'Паразитизм',
            #'Симбиоз',
            'A',
            'B',
            'C',
            
            
        ]
        # Задаем координаты верхнего левого угла меню:
        self.x = 50
        self.y = 300
        # Создаем список кнопок:
        self.buttons1 = []
        # Рассчитываем высоту для каждой кнопки меню, исходя и общей высоты:
        button_height1 = int(h / (len(self.labels) + 1))
        # Локальная переменная, хранит y координату для текущей кнопки:
        current_y = self.y
        for label in self.labels:
            # Создаем новую кнопку:
            new_button = Button(self.x, current_y, w, button_height1, label)
            # Переходим по вертикали к следующей кнопке с отступом в 2 пикселя,
            # чтобы кнопки визуально не "слиплись" между собой:
            current_y += button_height1 + 2
            # Добавляем новую кнопку в список всех кнопок меню:
            self.buttons1.append(new_button)

    # Вызвать метод update() для всех кнопок в меню:
    def update(self):
        for button in self.buttons1:
            button.update()

    # Вызвать метод обработки события для всех кнопок в меню:
    def handle_mouse_event(self, event):
        for button in self.buttons1:
            button.handle_mouse_action(event)
            # запоминаем и возвращаем кнопку, на которую сейчас нажали:
            if button.state == 'active':
                return button

    # Вызвать метод draw для всех кнопок в меню
    def draw(self, screen):
        for button in self.buttons1:
            button.draw(screen)

class ButtonForTask2():
    def __init__(self, w, h):
        # Создаем список пунктов меню:
        self.labels = [
            #Альберт Эйнштейн 
            #Никола Тесла
            #Исаак Ньютон
            'A',
            'B',
            'C',         
            
        ]
        # Задаем координаты верхнего левого угла меню:
        self.x = 50
        self.y = 300
        # Создаем список кнопок:
        self.buttons2 = []
        # Рассчитываем высоту для каждой кнопки меню, исходя и общей высоты:
        button_height2 = int(h / (len(self.labels) + 1))
        # Локальная переменная, хранит y координату для текущей кнопки:
        current_y = self.y
        for label in self.labels:
            # Создаем новую кнопку:
            new_button = Button(self.x, current_y, w, button_height2, label)
            # Переходим по вертикали к следующей кнопке с отступом в 2 пикселя,
            # чтобы кнопки визуально не "слиплись" между собой:
            current_y += button_height2 + 2
            # Добавляем новую кнопку в список всех кнопок меню:
            self.buttons2.append(new_button)

    # Вызвать метод update() для всех кнопок в меню:
    def update(self):
        for button in self.buttons2:
            button.update()

    # Вызвать метод обработки события для всех кнопок в меню:
    def handle_mouse_event(self, event):
        for button in self.buttons2:
            button.handle_mouse_action(event)
            # запоминаем и возвращаем кнопку, на которую сейчас нажали:
            if button.state == 'active':
                return button

    # Вызвать метод draw для всех кнопок в меню
    def draw(self, screen):
        for button in self.buttons2:
            button.draw(screen)

class ButtonForTask3():
    def __init__(self, w, h):
        # Создаем список пунктов меню:
        self.labels = [
            #дом 7 улица медведя
            #дом 5 улица малой медведицы
            #дом 2 город малой медведицы
            'A',
            'B',
            'C',         
            
        ]
        # Задаем координаты верхнего левого угла меню:
        self.x = 50
        self.y = 400
        # Создаем список кнопок:
        self.buttons3 = []
        # Рассчитываем высоту для каждой кнопки меню, исходя и общей высоты:
        button_height3 = int(h / (len(self.labels) + 1))
        # Локальная переменная, хранит y координату для текущей кнопки:
        current_y = self.y
        for label in self.labels:
            # Создаем новую кнопку:
            new_button = Button(self.x, current_y, w, button_height3, label)
            # Переходим по вертикали к следующей кнопке с отступом в 2 пикселя,
            # чтобы кнопки визуально не "слиплись" между собой:
            current_y += button_height3 + 2
            # Добавляем новую кнопку в список всех кнопок меню:
            self.buttons3.append(new_button)

    # Вызвать метод update() для всех кнопок в меню:
    def update(self):
        for button in self.buttons3:
            button.update()

    # Вызвать метод обработки события для всех кнопок в меню:
    def handle_mouse_event(self, event):
        for button in self.buttons3:
            button.handle_mouse_action(event)
            # запоминаем и возвращаем кнопку, на которую сейчас нажали:
            if button.state == 'active':
                return button

    # Вызвать метод draw для всех кнопок в меню
    def draw(self, screen):
        for button in self.buttons3:
            button.draw(screen)

class ButtonForTask4():
    def __init__(self, w, h):
        # Создаем список пунктов меню:
        self.labels = [
            #Пусть войны не будет
            #Пусть Китай станет частью России
            #Чтобы уроки сами делались
            'A',
            'B',
            'C',         
            
        ]
        # Задаем координаты верхнего левого угла меню:
        self.x = 500
        self.y = 400
        # Создаем список кнопок:
        self.buttons4 = []
        # Рассчитываем высоту для каждой кнопки меню, исходя и общей высоты:
        button_height4 = int(h / (len(self.labels) + 1))
        # Локальная переменная, хранит y координату для текущей кнопки:
        current_y = self.y
        for label in self.labels:
            # Создаем новую кнопку:
            new_button = Button(self.x, current_y, w, button_height4, label)
            # Переходим по вертикали к следующей кнопке с отступом в 2 пикселя,
            # чтобы кнопки визуально не "слиплись" между собой:
            current_y += button_height4 + 2
            # Добавляем новую кнопку в список всех кнопок меню:
            self.buttons4.append(new_button)

    # Вызвать метод update() для всех кнопок в меню:
    def update(self):
        for button in self.buttons4:
            button.update()

    # Вызвать метод обработки события для всех кнопок в меню:
    def handle_mouse_event(self, event):
        for button in self.buttons4:
            button.handle_mouse_action(event)
            # запоминаем и возвращаем кнопку, на которую сейчас нажали:
            if button.state == 'active':
                return button

    # Вызвать метод draw для всех кнопок в меню
    def draw(self, screen):
        for button in self.buttons4:
            button.draw(screen)
    
