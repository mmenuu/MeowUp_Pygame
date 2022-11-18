import pygame,sys
import pygame, sys
from settings import * 
from level import Level
from overworld import Overworld
from ui import UI
from button import Button
from game import Game

#pygame setup
pygame.init()

screen = pygame.display.set_mode((screen_width,screen_height)) 
clock = pygame.time.Clock()
# level = Level(level_0,screen)
font = pygame.font.Font('../fonts/font.ttf',30)
sec = 0
sec_count = 0
state = 1
game = Game()

def game():
    while True:
        # global game_status
        # game_status = 1
        screen.fill('Grey')
        # if game_status == 1:
        game.run()
        # elif game_status == 0:
            # level.check_game_over()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() 
                sys.exit()
        pygame.display.update()
        clock.tick(60)

def menu():
    while True :
        global game_status
        game_status = 1
        if game_status == 1:
            game_status = 0
            bg_menu = pygame.image.load('../graphics/menu/Background.png')
            screen.blit(bg_menu,(0,0))
            play_button = pygame.Rect((screen_width/2 - 100,screen_height/2-110),(210,130))
            score_button = pygame.Rect((screen_width/2 - 100,screen_height/2 + 85),(210,130))
            
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()            
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx,my = pygame.mouse.get_pos()
                    print(mx,'\n',my)
                    if play_button.collidepoint((mx,my)):
                        name()
                    if score_button.collidepoint((mx,my)):
                        score()
                    return state == 0      
        pygame.display.update()
        clock.tick(60)

def score():
    while True:
        bg_score = pygame.image.load('../graphics/menu/Background.png')
        screen.blit(bg_score,(0,0))
        back_button = pygame.Rect((screen_width-250,screen_height-100),(200,75))
        # pygame.draw.rect(screen,(0,0,0),back_button)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() 
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx,my = pygame.mouse.get_pos()
                    if back_button.collidepoint((mx,my)):
                        menu()
        pygame.display.update()
        clock.tick(60)
        
# def ranking():
#     global time 
#     time = []
#     scores = []
#     rankscores = []
#     with open('score.txt') as file:
#         for line in file:
#             name, score = line.split(',')
#             score = int(score)
#             scores.append((name, score))
#         scores.sort(key=lambda s: s[1])
#         scores.reverse()
#         for num in range(0, 5):
#             rankscores.insert(num,scores[num])
#         file.flush()


def display_text(text, size, color, pos, screen):
    font = pygame.font.Font('../fonts/font.ttf', size)
    text_surf = font.render(f'{text}', False, color)
    text_rect = text_surf.get_rect(center=pos)
    screen.blit(text_surf, text_rect)

def name():
    name_input = ''
    text_box = pygame.Rect((screen_width/2 - 225, screen_height/2 - 35), (480, 80))
    # start_button = pygame.Rect((1000,700),(100,50))
    # pygame.draw.rect(screen,('black'),start_button)
    active = False
    while True:
        # name_button = pygame.Rect((screen_width - 250, screen_height/2 + 200), (150, 60))
     
        # pygame.draw.rect(screen, ('black'), name_button)
        start_button = pygame.Rect((screen_width/2 + 330,screen_height/4+400),(200,80))
        back_button = pygame.Rect((screen_width/2 + 120,screen_height/4+400),(180,80))
        display_text('start', 30, ('white'), (screen_width - 175, screen_height/2 + 200 + 30), screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if text_box.collidepoint((mx,my)):
                    active = True
                else:
                    active = False
                if start_button.collidepoint((mx,my)):
                    game()
                if back_button.collidepoint((mx,my)):
                    menu()
                    
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_BACKSPACE:
                        name_input = name_input[:-1]
                    else:
                        name_input += event.unicode
                        print(event.unicode)
                        if surf.get_width() > text_box.w - 20:
                            name_input = name_input[:-1]
        # display_text(f'SCORE : {prev_player_score}', 20,('black'), (screen_width/2, 180), screen)
        # display_text('TYPE YOUR NAME', 20,('black'), (screen_width/2, 300), screen)
        if active:
            name_bg = pygame.image.load('../graphics/menu/Background.png')
        else:
            name_bg = pygame.image.load('../graphics/menu/Background.png')
        screen.blit(name_bg,(0,0))
        # start_button = pygame.Rect((screen_width/2 + 330,screen_height/4+400),(200,80))
        # back_button = pygame.Rect((screen_width/2 + 120,screen_height/4+400),(180,80))
        # pygame.draw.rect(screen,('black'),start_button)
        # pygame.draw.rect(screen,('black'),back_button)
        # for event in pygame.event.get():
        #     if event.type == pygame.MOUSEBUTTONDOWN:
        #         mx, my = pygame.mouse.get_pos()
        #         if start_button.collidepoint((mx,my)):
        #             game()
        #         if back_button.collidepoint((mx,my)):
        #             menu()
        surf = font.render(name_input, True, 'black')
        screen.blit(surf, (text_box.x + 5, text_box.y + 20))
        pygame.display.update()
        clock.tick(60)

# def over_win():
#     global status
#     if status == 1:
#         back_button = pygame.Rect((screen_width/2 + 120,screen_height/4+400),(180,80))
#         resume_button = pygame.Rect((screen_width/2 + 330,screen_height/4+400),(200,80))
#         pygame.draw.rect(screen,('black'),back_button)
#         pygame.draw.rect(screen,('black'),resume_button)

menu()