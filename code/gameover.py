# import pygame, sys
# from settings import * 
# from main import *

# def gameover():
#     user_ip = ''
#     text_box = pygame.Rect((screen_width/2 - 350/2, screen_height/2 - 20), (350, 50))
#     active = False
#     while True:
#         screen.fill("white")
#         screen.blit(BG, (0, 0))
#         menu_button = pygame.Rect((screen_width/2 -75, screen_height/2 + 200), (150, 60))
#         pygame.draw.rect(screen, ('violet'), menu_button)
#         display_text('BACK', 30, 'white', (screen_width/2, screen_height/2 + 200 +30), screen)
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 mx, my = pygame.mouse.get_pos()
#                 if text_box.collidepoint(event.pos):
#                     active = True
#                 else:
#                     active = False
#                 if menu_button.collidepoint((mx, my)):
#                     file = open('score.txt', 'a')
#                     file.write(f'{user_ip}, {prev_player_score}\n')
#                     file.flush()
#                     file.close()
#                     main_menu()
#             if event.type == pygame.KEYDOWN:
#                 if active:
#                     if event.key == pygame.K_BACKSPACE:
#                         user_ip = user_ip[:-1]
#                     else:
#                         user_ip += event.unicode
#                         if surf.get_width() > text_box.w - 20:
#                             user_ip = user_ip[:-1]
#         display_text('GAME OVER', 80, ('red'), (screen_width / 2, 170), screen)
#         display_text(f'SCORE : {prev_player_score}', 20,('white'), (screen_width/2, 250), screen)
#         display_text('ENTER YOUR NAME', 20,('white'), (screen_width/2, 300), screen)
#         if active:
#             color = pygame.Color('white')
#         else:
#             color = pygame.Color('red')
#         pygame.draw.rect(screen, color, text_box)
#         surf = get_font(20).render(user_ip, True, 'violet')
#         screen.blit(surf, (text_box.x + 5, text_box.y + 20))
#         pygame.display.update()
#         clock.tick(60)
