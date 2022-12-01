import pygame
import game_object
from constants import *
from game_menu import *
import game_menu
from button_for_task import*

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([WIN_WIDTH, WIN_HEIGHT])
        pygame.display.set_caption('Путешествия во времени')
        self.background_img = pygame.image.load("background1.png").convert()
        self.all_sprite_list = pygame.sprite.Group()
        self.frends_list = pygame.sprite.Group()

        # Создаем спрайт игрока
        self.player = game_object.Player(400, 0)
        # Создаем спрайт дедушки
        self.grandfather = game_object.Grandfather(350,300)
        #машина времени
        self.time_machine = game_object.TimeMachine(30,350)
        #frend1
        self.frend1 = game_object.Frends1(500,350)
        #frend2
        self.frend2 = game_object.Frends2(700,360)
        # Создаем спрайт BB-8
        self.bb8 = game_object.BB8(700,400)
        #добавляем спрайты в группы
        self.all_sprite_list.add(self.player)
        self.all_sprite_list.add(self.time_machine)
        self.all_sprite_list.add(self.bb8)
        self.frends_list.add(self.frend1)
        self.frends_list.add(self.frend2)
        self.all_sprite_list.add(self.grandfather)
        
        # Создаем главное меню
        self.top_panel = TopPanel(20, 10)
        self.timer_label = game_menu.TimerLabel
        self.main_menu = MainMenu(300, 200)
        # Создаем меню настроек
        self.settings_menu = SettingsMenu(300, 200)
        # Создаем кнопки для задания 1
        self.button5 = ButtonForTask5(200, 200)
        # Создаем кнопки для задания 2
        self.button6 = ButtonForTask6(200, 200)
        # Создаем кнопки для задания 3
        self.button1 = ButtonForTask1(200, 200)
        # Создаем кнопки для задания 4
        self.button2 = ButtonForTask2(200, 200)
        # Создаем кнопки для задания 5
        self.button3 = ButtonForTask3(200, 200)
        # Создаем кнопки для вопроса
        self.button4 = ButtonForTask4(200, 200)

        # Программируем смещение грового мира:
        self.shift = 0
        self.player_global_x = self.player.rect.x
        self.game_width = self.background_img.get_rect().width

        self.clock = pygame.time.Clock()
        # Будем вести отсчет игрового времени:
        self.time = 0
        # время столкновения с противником:
        # нужно для того, чтобы игрок не получал урон от противника чаще чем раз в секунду
        self.hit_time = 0

        # Игровые сцены state: 'START', MENU', 'SETTINGS', 'PLAYER', 'GAME', 'PAUSE', 'FINISH', 'GAME_OVER'
        self.state = 'START'
                


    # Обработка события для разных сотояний в игре
    def handle_states(self, event):
        # Обработка событий стартового экрана
        if self.state in ['START', 'FINISH', 'GAME OVER']:
            # Нажали на любую клавишу
            if event.type == pygame.KEYDOWN:
                self.state = 'MENU'

        # Обрабатываем события главного меню:
        elif self.state in ['MENU', 'PAUSE']:
            # Получаем кнопку, на которую нажали в главном меню:
            active_button = self.main_menu.handle_mouse_event(event.type)

            if active_button:
                # После того, как на кнопку нажали, возвращаем ее состояние в "normal":
                active_button.state =  'normal'

                # Нажали на кнопку START, начинаем игру 
                if active_button.name == 'START':
                    self.__init__()
                    self.state = 'SCENE1'

                # На паузе и нажали CONTINUE, переведем игру с состояние GAME:
                elif active_button.name == 'SKIP':
                    self.state = 'GAME'
                
                # На паузе и нажали ABOUT THE GAME, переведем игру с состояние ABOUT THE GAME:
                elif active_button.name == 'ABOUT THE GAME':
                    self.state = 'ABOUT THE GAME'                    

                # Вызвали меню настроек:
                elif active_button.name == 'SETTINGS':
                    self.state = 'SETTINGS'

                # Вызвали настройки игрока:
                elif active_button.name == 'PLAYER':
                    self.state = 'PLAYER'

                # Нажали на QUIT - завершим работу приложения:
                elif active_button.name == 'QUIT':
                    pygame.quit()

        elif self.state == 'TASK1':
            # Получаем кнопку, на которую нажали 
            active_button = self.button5.handle_mouse_event(event.type)

            if active_button:
                # После того, как на кнопку нажали, возвращаем ее состояние в "normal":
                active_button.state =  'normal'

                # Нажали на кнопку 
                if active_button.name == 'C':
                    self.player.lives -= 1
                    if self.player.score >= 1:
                        self.player.score -= 1
                    print(active_button.name)
                    self.state = 'OTVET10'
                elif active_button.name == 'B':
                    self.player.lives -= 1
                    if self.player.score >= 1:
                        self.player.score -= 1
                    print(active_button.name)
                    self.state = 'OTVET10'
                elif active_button.name == 'A':
                    self.player.score += 1
                    print(active_button.name)
                    self.state = 'OTVET9'
        
        elif self.state == 'TASK2':
            # Получаем кнопку, на которую нажали 
            active_button = self.button6.handle_mouse_event(event.type)

            if active_button:
                # После того, как на кнопку нажали, возвращаем ее состояние в "normal":
                active_button.state =  'normal'

                # Нажали на кнопку 
                if active_button.name == 'C':
                    self.player.lives -= 1
                    if self.player.score >= 1:
                        self.player.score -= 1
                    print(active_button.name)
                    self.state = 'OTVET12'
                elif active_button.name == 'B':
                    self.player.lives -= 1
                    if self.player.score >= 1:
                        self.player.score -= 1
                    print(active_button.name)
                    self.state = 'OTVET12'
                elif active_button.name == 'A':
                    self.player.score += 1
                    print(active_button.name)
                    self.state = 'OTVET11'

        elif self.state == 'TASK3':
            # Получаем кнопку, на которую нажали 
            active_button = self.button1.handle_mouse_event(event.type)

            if active_button:
                # После того, как на кнопку нажали, возвращаем ее состояние в "normal":
                active_button.state =  'normal'

                # Нажали на кнопку 
                if active_button.name == 'A':
                    self.player.lives -= 1
                    if self.player.score >= 1:
                        self.player.score -= 1
                    print(active_button.name)
                    self.state = 'OTVET'
                elif active_button.name == 'B':
                    self.player.lives -= 1
                    if self.player.score >= 1:
                        self.player.score -= 1
                    print(active_button.name)
                    self.state = 'OTVET'
                elif active_button.name == 'C':
                    self.player.score += 1
                    print(active_button.name)
                    self.state = 'OTVET1'
        
        elif self.state == 'TASK4':
            # Получаем кнопку, на которую нажали 
            active_button = self.button2.handle_mouse_event(event.type)

            if active_button:
                # После того, как на кнопку нажали, возвращаем ее состояние в "normal":
                active_button.state =  'normal'

                # Нажали на кнопку 
                if active_button.name == 'A':
                    self.player.lives -= 1
                    if self.player.score >= 1:
                        self.player.score -= 1
                    print(active_button.name)
                    self.state = 'OTVET2'
                elif active_button.name == 'B':
                    self.player.lives -= 1
                    if self.player.score >= 1:
                        self.player.score -= 1
                    print(active_button.name)
                    self.state = 'OTVET2'
                elif active_button.name == 'C':
                    self.player.score += 1
                    print(active_button.name)
                    self.state = 'OTVET3'
        
        elif self.state == 'TASK5':
            # Получаем кнопку, на которую нажали 
            active_button = self.button3.handle_mouse_event(event.type)

            if active_button:
                # После того, как на кнопку нажали, возвращаем ее состояние в "normal":
                active_button.state =  'normal'

                # Нажали на кнопку 
                if active_button.name == 'A':
                    self.player.lives -= 1
                    if self.player.score >= 1:
                        self.player.score -= 1
                    print(active_button.name)
                    self.state = 'OTVET4'
                elif active_button.name == 'B':
                    self.player.score += 1
                    print(active_button.name)
                    self.state = 'OTVET5'
                elif active_button.name == 'C':
                    self.player.lives -= 1
                    if self.player.score >= 1:
                        self.player.score -= 1
                    print(active_button.name)
                    self.state = 'OTVET4'
        
        elif self.state == 'TASK6':
            # Получаем кнопку, на которую нажали 
            active_button = self.button4.handle_mouse_event(event.type)

            if active_button:
                # После того, как на кнопку нажали, возвращаем ее состояние в "normal":
                active_button.state =  'normal'

                # Нажали на кнопку 
                if active_button.name == 'A':
                    self.player.score += 1
                    print(active_button.name)
                    self.state = 'OTVET8'
                elif active_button.name == 'B':
                    self.player.score += 1
                    print(active_button.name)
                    self.state = 'OTVET6'
                elif active_button.name == 'C':
                    self.player.score += 1
                    print(active_button.name)
                    self.state = 'OTVET7'
                    

    
        #обрабатываем события смены сцены
        elif self.state == 'SCENE1':
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    self.state = 'SCENE2'
        elif self.state == 'SCENE2':
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    self.state = 'SCENE3'     
        elif self.state == 'SCENE3':
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    self.state = 'GAME'
        elif self.state == 'SCENE4':
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    self.state = 'SCENE5'
        elif self.state == 'SCENE5':
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    self.state = 'SCENE6'
        elif self.state == 'SCENE6':
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    self.state = 'TASK1'
        elif self.state == 'OTVET9':
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    self.state = 'SCENE7'   
        elif self.state == 'OTVET10':
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    self.state = 'SCENE7' 
        elif self.state == 'SCENE10':
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    self.state = 'SCENE11'
        elif self.state == 'SCENE11':
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    self.state = 'TASK3'
        elif self.state == 'OTVET':
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    self.state = 'SCENE12'
        elif self.state == 'OTVET1':
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    self.state = 'SCENE12'
        elif self.state == 'SCENE12':
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    self.state = 'SCENE13'
        elif self.state == 'SCENE13':
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    self.state = 'TASK4' 
        elif self.state == 'OTVET2':
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    self.state = 'SCENE14'
        elif self.state == 'OTVET3':
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    self.state = 'SCENE14'
        elif self.state == 'SCENE14':
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    self.state = 'SCENE15'
        elif self.state == 'SCENE15':
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    self.state = 'TASK5'
        elif self.state == 'OTVET4':
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    self.state = 'SCENE16'
        elif self.state == 'OTVET5':
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    self.state = 'SCENE16'
        elif self.state == 'SCENE16':
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    self.state = 'TASK6'
        elif self.state == 'OTVET6':
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    self.state = 'GAME2'
        elif self.state == 'OTVET7':
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    self.state = 'GAME2'
        elif self.state == 'OTVET8':
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    self.state = 'GAME2'
        elif self.state == 'SCENE7':
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    self.state = 'SCENE8'
        elif self.state == 'SCENE8':
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    self.state = 'SCENE9'    
        elif self.state == 'SCENE9':
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    self.state = 'TASK2'  
        elif self.state == 'OTVET11':
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    self.state = 'SCENE10'  
        elif self.state == 'OTVET12':
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    self.state = 'SCENE10'  

        elif self.state == 'ABOUT THE GAME':
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.state = 'MENU'
        
        elif self.state == 'SCENE17':
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z and self.player.lives >= 1:
                    self.state = 'FINISH'
                elif event.key == pygame.K_z and self.player.lives < 1:
                    self.state = 'GAME_OVER'                
        
        #elif self.state == 'PLAYER':
            #if event.type == pygame.KEYDOWN:
             #   if event.key == pygame.K_1:
              #      self.player.img0 = 'boy.png'
               #     self.player.img1 = 'boy1.png'
               #     self.player.img2 = 'boy5.png'
               # elif event.key == pygame.K_2:
               #     self.player.img0 = 'girl.png'
               #     self.player.img1 = 'girl1.png'
               #     self.player.img2 = 'girl4.png'
        


        # Обработка событий, когда идет игра
        elif self.state == 'GAME':
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.go_left()
                elif event.key == pygame.K_RIGHT:
                    self.player.go_right()
                elif event.key == pygame.K_UP:
                    self.player.jump()
                elif event.key == pygame.K_a:
                    self.player.go_left()
                elif event.key == pygame.K_d:
                    self.player.go_right()
                elif event.key == pygame.K_w:
                    self.player.jump()

            elif event.type == pygame.KEYUP:
                if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and self.player.change_x < 0:
                    self.player.stop()
                if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and self.player.change_x > 0:
                    self.player.stop()
                elif event.key == pygame.K_ESCAPE and self.state == 'START':
                    self.state = 'MENU'
                elif event.key == pygame.K_q:
                    self.state = 'SCENE4' 
        # Обработка событий, когда идет игра2
        elif self.state == 'GAME2':
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.go_left()
                elif event.key == pygame.K_RIGHT:
                    self.player.go_right()
                elif event.key == pygame.K_UP:
                    self.player.jump()
                elif event.key == pygame.K_a:
                    self.player.go_left()
                elif event.key == pygame.K_d:
                    self.player.go_right()
                elif event.key == pygame.K_w:
                    self.player.jump()

            elif event.type == pygame.KEYUP:
                if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and self.player.change_x < 0:
                    self.player.stop()
                if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and self.player.change_x > 0:
                    self.player.stop()
                elif event.key == pygame.K_q:
                    self.state = 'SCENE17' 
                
        
    # Прорисовка сцены
    def draw(self):
        # Выполняем заливку фона:
        self.screen.fill(BLACK)
        if self.state == 'START':
            # Рисуем заставку
            self.screen.blit(pygame.image.load("background7.png").convert(), [0, 0])
        elif self.state == 'MENU':
            # Заливаем фон
            self.screen.blit(pygame.image.load("background6.png").convert(), [0, 0])
            # Рисуем главное меню:
            self.main_menu.draw(self.screen)
        elif self.state == 'SETTINGS':
            # Заливаем фон
            self.screen.blit(pygame.image.load("background6.png").convert(), [0, 0])
            # Рисуем меню настроек:
            self.settings_menu.draw(self.screen)
        elif self.state == 'SCENE1':
            # Выполняем заливку фона:
            self.screen.blit(pygame.image.load("background9.png").convert(), [0, 0])
        elif self.state == 'SCENE2':
            # Выполняем заливку фона:
            self.screen.blit(pygame.image.load("background10.png").convert(), [0, 0])
        elif self.state == 'SCENE3':
            # Выполняем заливку фона:
            self.screen.blit(pygame.image.load("background11.png").convert(), [0, 0])
        elif self.state == 'ABOUT THE GAME':
            #заливка фона
            self.screen.blit(pygame.image.load("ABOUT THE GAME.png").convert(), [0, 0])
        elif self.state == 'SCENE4':
            # Выполняем заливку фона:
            self.screen.blit(pygame.image.load("background23.png").convert(), [0, 0])
        elif self.state == 'SCENE5':
            # Выполняем заливку фона:
            self.screen.blit(pygame.image.load("background24.png").convert(), [0, 0])
        elif self.state == 'SCENE6':
            # Выполняем заливку фона:
            self.screen.blit(pygame.image.load("background13.png").convert(), [0, 0])
            self.screen.blit(pygame.image.load("text3.png").convert(), [0, 0])
        elif self.state == 'SCENE10':
            # Выполняем заливку фона:
            self.screen.blit(pygame.image.load("background17.png").convert(), [0, 0])
            self.screen.blit(pygame.image.load("text5.png").convert(), [0, 0])
        elif self.state == 'SCENE11':
            # Выполняем заливку фона:
            self.screen.blit(pygame.image.load("background18.png").convert(), [0, 0])
            self.screen.blit(pygame.image.load("text4.png").convert(), [0, 0])
        elif self.state == 'TASK3':
            # Выполняем заливку фона:
            self.screen.blit(pygame.image.load("task3.png").convert(), [0, 0])
            self.button1.draw(self.screen)
        elif self.state == 'OTVET':
            # Выполняем заливку фона:
            self.screen.blit(pygame.image.load("OTVET.png").convert(), [0, 0])
        elif self.state == 'OTVET1':
            # Выполняем заливку фона:
            self.screen.blit(pygame.image.load("OTVET1.png").convert(), [0, 0])
        elif self.state == 'OTVET10':
            # Выполняем заливку фона:
            self.screen.blit(pygame.image.load("OTVET.png").convert(), [0, 0])
        elif self.state == 'OTVET9':
            # Выполняем заливку фона:
            self.screen.blit(pygame.image.load("OTVET1.png").convert(), [0, 0])
        elif self.state == 'SCENE12':
            # Выполняем заливку фона:
            self.screen.blit(pygame.image.load("background19.png").convert(), [0, 0])
            self.screen.blit(pygame.image.load("text6.png").convert(), [0, 0])
        elif self.state == 'SCENE13':
            # Выполняем заливку фона:
            self.screen.blit(pygame.image.load("background20.png").convert(), [0, 0])
            self.screen.blit(pygame.image.load("text7.png").convert(), [0, 0])
        elif self.state == 'TASK4':
            # Выполняем заливку фона:
            self.screen.blit(pygame.image.load("task4.png").convert(), [0, 0])
            self.button2.draw(self.screen)
        elif self.state == 'OTVET2':
            # Выполняем заливку фона:
            self.screen.blit(pygame.image.load("OTVET.png").convert(), [0, 0])
        elif self.state == 'OTVET3':
            # Выполняем заливку фона:
            self.screen.blit(pygame.image.load("OTVET1.png").convert(), [0, 0])
        elif self.state == 'SCENE14':
            # Выполняем заливку фона:
            self.screen.blit(pygame.image.load("background21.png").convert(), [0, 0])
            self.screen.blit(pygame.image.load("text8.png").convert(), [0, 0])
        elif self.state == 'SCENE15':
            # Выполняем заливку фона:
            self.screen.blit(pygame.image.load("background22.png").convert(), [0, 0])
            self.screen.blit(pygame.image.load("grandfather.png"), [10, 300])
            self.screen.blit(pygame.image.load("boy.png"), [100, 360])
            self.screen.blit(pygame.image.load("BB-8.png"), [200, 400])
            self.screen.blit(pygame.image.load("text9.png"), [200, 300])
            self.screen.blit(pygame.image.load("text10.png"), [400, 220])
            self.screen.blit(pygame.image.load("text11.png"), [500, 120])
            self.frends_list.draw(self.screen)
        elif self.state == 'TASK5':
            # Выполняем заливку фона:
            self.screen.blit(pygame.image.load("task5.png").convert(), [0, 0])
            self.button3.draw(self.screen)        
        elif self.state == 'OTVET4':
            # Выполняем заливку фона:
            self.screen.blit(pygame.image.load("OTVET2.png").convert(), [0, 0])
        elif self.state == 'OTVET5':
            # Выполняем заливку фона:
            self.screen.blit(pygame.image.load("OTVET3.png").convert(), [0, 0])
        elif self.state == 'SCENE16':
            # Выполняем заливку фона:
            self.screen.blit(pygame.image.load("background25.png").convert(), [0, 0])
        elif self.state == 'TASK6':
            # Выполняем заливку фона:
            self.screen.blit(pygame.image.load("task6.png").convert(), [0, 0])
            self.button4.draw(self.screen) 
        elif self.state == 'OTVET6':
            # Выполняем заливку фона:
            self.screen.blit(pygame.image.load("OTVET6.png").convert(), [0, 0])
        elif self.state == 'OTVET7':
            # Выполняем заливку фона:
            self.screen.blit(pygame.image.load("OTVET7.png").convert(), [0, 0])
        elif self.state == 'OTVET8':
            # Выполняем заливку фона:
            self.screen.blit(pygame.image.load("OTVET8.png").convert(), [0, 0])
        elif self.state == 'GAME2':
            # Выполняем заливку фона:
            self.screen.blit(pygame.image.load("background12.png").convert(), [0, 0])
            # Рисуем все спрайты в игре:
            self.top_panel.draw(self.screen)
            self.all_sprite_list.draw(self.screen)
            self.screen.blit(pygame.image.load("text12.png").convert(), [0, 0])
            self.screen.blit(pygame.image.load("text13.png").convert(), [500, 300])
            self.screen.blit(pygame.image.load("text14.png").convert(), [250, 250])
        elif self.state == 'SCENE17':
            # Выполняем заливку фона:
            self.screen.blit(pygame.image.load("background1.png").convert(), [0, 0])
            self.screen.blit(pygame.image.load('time_machine.png'), [300, 350])
            self.screen.blit(pygame.image.load('grandfather.png'), [10, 300])
            self.screen.blit(pygame.image.load('boy.png'), [100, 360])
            self.screen.blit(pygame.image.load('text15.png').convert(), [0, 0])
        elif self.state == 'SCENE7':
            # Выполняем заливку фона:
            self.screen.blit(pygame.image.load("background14.png").convert(), [0, 0])
            self.screen.blit(pygame.image.load('text16.png').convert(), [0, 0])
        elif self.state == 'TASK1':
            # Выполняем заливку фона:
            self.screen.blit(pygame.image.load("task1.png").convert(), [0, 0])
            self.button5.draw(self.screen)
        elif self.state == 'SCENE8':
            # Выполняем заливку фона:
            self.screen.blit(pygame.image.load("background15.png").convert(), [0, 0])
            self.screen.blit(pygame.image.load('text17.png').convert(), [0, 0])
        elif self.state == 'SCENE9':
            # Выполняем заливку фона:
            self.screen.blit(pygame.image.load("background16.png").convert(), [0, 0])
            self.screen.blit(pygame.image.load('text18.png').convert(), [0, 0])
        elif self.state == 'TASK2':
            # Выполняем заливку фона:
            self.screen.blit(pygame.image.load("task2.png").convert(), [0, 0])
            self.button6.draw(self.screen)
        elif self.state == 'OTVET11':
            # Выполняем заливку фона:
            self.screen.blit(pygame.image.load("OTVET1.png").convert(), [0, 0])
        elif self.state == 'OTVET12':
            # Выполняем заливку фона:
            self.screen.blit(pygame.image.load("OTVET.png").convert(), [0, 0])



        elif self.state == 'GAME':
            # Выполняем заливку фона:
            self.screen.blit(pygame.image.load("background12.png").convert(), [0, 0])
            # Рисуем все спрайты в игре:
            self.top_panel.draw(self.screen)
            self.all_sprite_list.draw(self.screen)
            self.screen.blit(pygame.image.load("text1.png").convert(), [400, 200])
            self.screen.blit(pygame.image.load("text2.png").convert(), [600, 300])
            self.screen.blit(pygame.image.load("text.png").convert(), [500, 0])

        elif self.state == 'FINISH':
            # Заливаем фон
            self.screen.blit(pygame.image.load("background3.png").convert(), [0, 0])
            self.top_panel.finish_screen(420, 345)
            self.top_panel.finish_screen_draw(self.screen)
        elif self.state == 'GAME_OVER':
            # Заливаем фон
            self.screen.blit(pygame.image.load("background3.png").convert(), [0, 0])
            self.top_panel.finish_screen(420, 345)
            self.top_panel.game_over_screen_draw(self.screen)

    # Обновление текущего состояния игры
    def update(self):
        # Если идет игра, обновляем все объекты в игре:
        if self.state == 'GAME':
            self.time += 1
            self.all_sprite_list.update()
            self.top_panel.update(coin=self.player.score, lives=self.player.lives)


        # Если игра в состоянии SETTINGS, обновляем меню настроек:
        elif self.state == 'SETTINGS':
            self.settings_menu.update() 
        #Обновляем кнопки для задания1
        elif self.state == 'TASK1':
            self.button5.update()
        #Обновляем кнопки для задания2
        elif self.state == 'TASK2':
            self.button6.update()
        #Обновляем кнопки для задания3
        elif self.state == 'TASK3':
            self.button1.update()
        #Обновляем кнопки для задания4
        elif self.state == 'TASK4':
            self.button2.update()
        #Обновляем кнопки для задания5
        elif self.state == 'TASK5':
            self.button3.update()
        #Обновляем кнопки для задания6
        elif self.state == 'TASK6':
            self.button4.update()
        elif self.state == 'GAME2':
            self.time += 1
            self.all_sprite_list.update()
            self.top_panel.update(coin=self.player.score, lives=self.player.lives)
        # Если игра на паузе или на старте, обновляем  меню:
        else:
            self.main_menu.update()
            

    def run(self):
        done = False
        # Запустили главный игровой цикл:
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                # Обрабатываем события для разных состояний:
                self.handle_states(event)

            # Если игрок приближается к правому краю экрана, смещаем мир влево на (-x)
            if self.player.rect.right >= 500 and abs(self.shift) < self.game_width - WIN_WIDTH:
                diff = self.player.rect.right - 500
                self.player.rect.right = 500
                self.shift_world(-diff)

            # Если игрок приближается к левому краю экрана, смещаем мир вправо на (+x)
            if self.player.rect.left <= 120 and abs(self.shift) > 0:
                diff = 120 - self.player.rect.left
                self.player.rect.left = 120
                self.shift_world(diff)

            self.update()
            # Отрисовываем окно игры для текущего состояния:
            self.draw()
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()

game = Game()
game.run()

