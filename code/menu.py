import pygame, sys
from settings import * 
from level import Level
from overworld import Overworld
from ui import UI
from button import Button
from game import Game


# Pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
game = Game()
running = True
start = False
game_status = 1
prev_player_score = 0
new_player_score = 0
scores = []
rankscores = []
show = 0

BG = pygame.image.load("../graphics/menu/Background.png")
name_BG = pygame.image.load("../graphics/menu/name.png")
LB = pygame.image.load("../graphics/menu/Leaderboard.png")


prev_player_score = 0
new_player_score = 0

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("../fonts/font.ttf", size)

def display_text(text, size, color, pos, screen):
    font = pygame.font.Font("../fonts/font.ttf", size)
    text_surf = font.render(f'{text}', False, color)
    text_rect = text_surf.get_rect(center=pos)
    screen.blit(text_surf, text_rect)
    
def scores():
    while True:
        scoreS_MOUSE_POS = pygame.mouse.get_pos()
        screen.fill("white")

        scoreS_TEXT = get_font(20).render("This is the scoreS screen.", True, "Black")
        scoreS_RECT = scoreS_TEXT.get_rect(center=(640, 260))
        screen.blit(scoreS_TEXT, scoreS_RECT)

        scoreS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        scoreS_BACK.changeColor(scoreS_MOUSE_POS)
        scoreS_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if scoreS_BACK.checkForInput(scoreS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu(running,start):
    global game_status,show
    show = 0
    while running:
        screen.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MEOW UP!", True, "White")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 250))
        

        PLAY_BUTTON = Button(image=pygame.image.load("../graphics/menu/Play Rect.png"), pos=(screen_width/2-200, 350), 
                            text_input="PLAY", font=get_font(30), base_color="White", hovering_color="Violet")
        scoreS_BUTTON = Button(image=pygame.image.load("../graphics/menu/Options Rect.png"), pos=(screen_width/2, 350), 
                            text_input="SCORE", font=get_font(30), base_color="White", hovering_color="Violet")
        QUIT_BUTTON = Button(image=pygame.image.load("../graphics/menu/Quit Rect.png"), pos=(screen_width/2+200, 350), 
                            text_input="QUIT", font=get_font(30), base_color="White", hovering_color="Violet")

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, scoreS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    screen.fill('black')
                    start = True
                if scoreS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    # scores()
                    rank()
                    # screen.fill("white")
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        if start:
            game.run()
            gamegame()
        pygame.display.update()
        
def gameover():
    user_ip = ''
    text_box = pygame.Rect((screen_width/2 - 350/2, screen_height/2 - 20), (350, 50))
    active = False
    while True:
        screen.fill("white")
        screen.blit(BG, (0, 0))
        menu_button = pygame.Rect((screen_width/2 -75, screen_height/2 + 200), (150, 60))
        pygame.draw.rect(screen, ('violet'), menu_button)
        display_text('BACK', 30, 'white', (screen_width/2, screen_height/2 + 200 +30), screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if text_box.collidepoint(event.pos):
                    active = True
                else:
                    active = False
                if menu_button.collidepoint((mx, my)):
                    file = open('score.txt', 'a')
                    file.write(f'{user_ip}, {prev_player_score}\n')
                    file.flush()
                    file.close()
                    main_menu()
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_BACKSPACE:
                        user_ip = user_ip[:-1]
                    else:
                        user_ip += event.unicode
                        if surf.get_width() > text_box.w - 20:
                            user_ip = user_ip[:-1]
        display_text('GAME OVER', 80, ('red'), (screen_width / 2, 170), screen)
        display_text(f'SCORE : {prev_player_score}', 20,('white'), (screen_width/2, 250), screen)
        display_text('ENTER YOUR NAME', 20,('white'), (screen_width/2, 300), screen)
        if active:
            color = pygame.Color('white')
        else:
            color = pygame.Color('red')
        pygame.draw.rect(screen, color, text_box)
        surf = get_font(20).render(user_ip, True, 'violet')
        screen.blit(surf, (text_box.x + 5, text_box.y + 20))
        pygame.display.update()
        clock.tick(60)

def draw_text_rank(text, color, size, screen, pos):
    font = pygame.font.Font('../fonts/font.ttf', size)
    textobj = font.render(text, False, color)
    textrect = textobj.get_rect(midleft = pos)
    screen.blit(textobj, textrect)

def ranking():
    global scores, rankscores, show
    if show != 1:
        scores = []
        rankscores = []
        with open('score.txt') as file:
            for line in file:
                name, score = line.split(',')
                score = int(score)
                scores.append((name, score))
            scores.sort(key=lambda s: s[1])
            scores.reverse()
            for num in range(0, 5):
                rankscores.insert(num,scores[num])
            file.flush()
            show = 1
def display_rank():
    ranking()
    space = 0
    for i in range(0, 5):
        draw_text_rank(f'{rankscores[i][0]}', ('white'), 20, screen, (screen_width / 2 - 250, 230 + space))
        space += 50
    space = 0
    for i in range(0, 5):
        draw_text_rank(f'{rankscores[i][1]}', ('white'), 20, screen, (screen_width / 2 + 200, 230 + space))
        space += 50
def gamegame():
    while True:
        global game_status, new_player_score, prev_player_score
        new_player_score = game.coins
        if new_player_score >= prev_player_score:
            prev_player_score = new_player_score
        if game_status == 1:
            game.run()
            game_status = game.game_status
            print(game_status)
        elif game_status == 0:
            gameover()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()  
        pygame.display.update()
        clock.tick(60)
def rank():
    while True:
        screen.fill("white")
        screen.blit(LB, (0, 0))
        menu_button = pygame.Rect(
            (screen_width - 250, screen_height/2 + 200), (150, 60))
        pygame.draw.rect(screen, ('violet'), menu_button)
        display_text('back', 30, 'white', (screen_width -
                     175, screen_height/2 + 200 + 30), screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if menu_button.collidepoint((mx, my)):
                    main_menu()
        display_rank()
        pygame.display.update()
        clock.tick(60)