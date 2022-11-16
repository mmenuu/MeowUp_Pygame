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

# while True:
# 	for event in pygame.event.get():
# 		if event.type == pygame.QUIT:
# 			pygame.quit()
# 			sys.exit()
	
# 	screen.fill('grey')
# 	game.run()

# 	pygame.display.update()
# 	clock.tick(60)


BG = pygame.image.load("../graphics/menu/Background.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("../fonts/font.ttf", size)

# def play():
#     while True:
#         PLAY_MOUSE_POS = pygame.mouse.get_pos()
#         screen.fill("black")
#         game.run()
        # PLAY_MOUSE_POS = pygame.mouse.get_pos()
        # PLAY_TEXT = get_font(20).render("This is the PLAY screen.", True, "White")
        # PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        # screen.blit(PLAY_TEXT, PLAY_RECT)

        # PLAY_BACK = Button(image=None, pos=(640, 460), 
        #                     text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        # PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        # PLAY_BACK.update(screen)

        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         pygame.quit()
        #         sys.exit()
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
            #         main_menu()
        # pygame.display.update()
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        screen.fill("white")

        OPTIONS_TEXT = get_font(20).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu(running,start):
    while running:
        screen.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MEOW UP!", True, "#FFFFFF")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 250))

        PLAY_BUTTON = Button(image=pygame.image.load("../graphics/menu/Play Rect.png"), pos=(640, 350), 
                            text_input="PLAY", font=get_font(30), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("../graphics/menu/Options Rect.png"), pos=(640, 400), 
                            text_input="SCORE", font=get_font(30), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("../graphics/menu/Quit Rect.png"), pos=(640, 500), 
                            text_input="QUIT", font=get_font(30), base_color="#d7fcd4", hovering_color="White")

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
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
                    #return start
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        if start:
            game.run()
        pygame.display.update()

main_menu(running,start)
