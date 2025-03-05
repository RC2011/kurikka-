import sys
import pygame
from pygame.locals import Rect
from LCD_font import LCD_font_styles
from LCD_font import LCD_font
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()

DARK_GRAY = (40, 40, 40)
GRAY = (80, 80, 80)
RED = (255, 0, 0)
GREEN = (10, 250, 10)
YELLOW = (250, 250, 20)
WHITE = (250, 250, 250)
BLUE = (100, 100, 255)
BLACK = (0, 0, 0)

LCD = LCD_font_styles
screen = pygame.display.set_mode([600, 600])
pygame.display.set_caption("pan clikker")
mouse_x, mouse_y = pygame.mouse.get_pos()
panseisan = 9
panseisan2 = 9
koeta = 0

screen.fill((100, 100, 255)) #RED, GREEN, BLUE

lcd2 = LCD_font(screen)
lcd2.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=BLACK, COLOR_OFF=BLUE)
lcd2.init_row(X_ORG=2, Y_ORG=3, COL_INTV=6)

lcd3 = LCD_font(screen)
lcd3.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=BLACK, COLOR_OFF=BLUE)
lcd3.init_row(X_ORG=2, Y_ORG=3, COL_INTV=6)

lcd4 = LCD_font(screen)
lcd4.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=BLACK, COLOR_OFF=BLUE)
lcd4.init_row(X_ORG=2, Y_ORG=3, COL_INTV=6)

lcd5 = LCD_font(screen)
lcd5.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=BLACK, COLOR_OFF=BLUE)
lcd5.init_row(X_ORG=2, Y_ORG=3, COL_INTV=6)

lcd6 = LCD_font(screen)
lcd6.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=BLACK, COLOR_OFF=BLUE)
lcd6.init_row(X_ORG=2, Y_ORG=3, COL_INTV=6)

lcd7 = LCD_font(screen)
lcd7.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=BLACK, COLOR_OFF=BLUE)
lcd7.init_row(X_ORG=2, Y_ORG=3, COL_INTV=6)

lcd8 = LCD_font(screen)
lcd8.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=BLACK, COLOR_OFF=BLUE)
lcd8.init_row(X_ORG=2, Y_ORG=3, COL_INTV=6)

code2 = 0
code3 = 0
code4 = 0
code5 = 0
code6 = 0
code7 = 0
code8 = 0

lcd2.update_col(col=6, code=code2)
lcd3.update_col(col=5, code=code3)
lcd4.update_col(col=4, code=code4)
lcd5.update_col(col=3, code=code5)
lcd6.update_col(col=2, code=code6)
lcd7.update_col(col=1, code=code7)
lcd8.update_col(col=0, code=code8)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if not running:
            break
        if mouse_x > 205:
            if mouse_x < 399:
                if mouse_y > 403:
                    if mouse_y < 489:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            code2= (code2 + 1)
                            if panseisan > 0:
                                code2= (code2 + 1)
                                panseisan= (panseisan - 1)
                                if panseisan > 0:
                                    code2= (code2 + 1)
                                    panseisan= (panseisan - 1)
                                    if panseisan > 0:
                                        code2= (code2 + 1)
                                        panseisan= (panseisan - 1)
                                        if panseisan > 0:
                                           code2= (code2 + 1)
                                           panseisan= (panseisan - 1)
                                           if panseisan > 0:
                                                code2= (code2 +1)
                                                panseisan= (panseisan - 1)
                                                if panseisan > 0:
                                                     code2= (code2 +1)
                                                     panseisan= (panseisan - 1)
                                                     if panseisan > 0:
                                                        code2= (code2 +1)
                                                        panseisan= (panseisan - 1)
                                                        if panseisan > 0:
                                                            code2= (code2 +1)
                                                            panseisan= (panseisan - 1)
                                                            if panseisan > 0:
                                                               code2= (code2 + 1)
                                                               panseisan= (panseisan - 1)
                                                               if panseisan > 0:
                                                                  if code2 > 8:
                                                                       koeta= (koeta + 1) 
                                                                  code2= (code2 + 1)
                                                                  panseisan= (panseisan - 1)
                                                                  if panseisan > 0:
                                                                     if code2 > 7:
                                                                          koeta= (koeta + 1) 
                                                                     code2= (code2 + 1)
                                                                     panseisan= (panseisan - 1)
                                                                     if panseisan > 0:
                                                                        if code2 > 6:
                                                                             koeta= (koeta + 1) 
                                                                        code2= (code2 + 1)
                                                                        panseisan= (panseisan - 1)
                                                                        if panseisan > 0:
                                                                           if code2 > 5:
                                                                                koeta= (koeta + 1) 
                                                                           code2= (code2 +1)
                                                                           panseisan= (panseisan - 1)
                                                                           if panseisan > 0:
                                                                              if code2 > 4:
                                                                                   koeta= (koeta + 1) 
                                                                              code2= (code2 +1)
                                                                              panseisan= (panseisan - 1)
                                                                              if panseisan > 0:
                                                                                 if code2 > 3:
                                                                                      koeta= (koeta + 1) 
                                                                                 code2= (code2 +1)
                                                                                 panseisan= (panseisan - 1)
                                                                                 if panseisan > 0:
                                                                                    if code2 > 2:
                                                                                         koeta= (koeta + 1) 
                                                                                    code2= (code2 +1)
                                                                                    panseisan= (panseisan - 1)
                                                                                    if panseisan > 0:
                                                                                       if code2 > 1:
                                                                                            koeta= (koeta + 1) 
                                                                                       code2= (code2 +1)
                                                                                       panseisan= (panseisan - 1)
                                                                                       if panseisan > 0:
                                                                                          if code2 > 0:
                                                                                               koeta= (koeta + 1) 
                                                                                          code2= (code2 +1)
                                                                                          panseisan= (panseisan - 1)
                                                                                          if panseisan > 0:
                                                                                             code2= (code2 +1)
                                                                                             panseisan= (panseisan - 1)
                                                                                             koeta= (koeta + 1)
                            if code3 == 9:
                                if code4 == 9:
                                    if code5 == 9:
                                        if code6 == 9:
                                            if code7 == 9:
                                                if code8 == 9:
                                                    if code2 < 10:
                                                        code2= (code2 - 1)
        if code2 > 9:
                    code3= (code3 + 1)
                    if koeta == 1:
                         code3= (code3 + 1)
                         koeta = 0
                    if code2 == 10:
                         code2 = 0
                    if code2 == 11:
                         code2 = 1
                    if code2 == 12:
                         code2 = 2
                    if code2 == 13:
                         code2 = 3
                    if code2 == 14:
                         code2 = 4
                    if code2 == 15:
                         code2 = 5
                    if code2 == 16:
                         code2 = 6
                    if code2 == 17:
                         code2 = 7
                    if code2 == 18:
                         code2 = 8
                    if code2 == 19:
                         code2 = 9
                    if code2 == 20:
                         code2 = 0
                    if code2 == 21:
                         code2 = 1
                    if code2 == 22:
                         code2 = 2
                    if code2 == 23:
                         code2 = 3
                    if code2 == 24:
                         code2 = 4
                    if code2 == 25:
                         code2 = 5
                    if code2 == 26:
                         code2 = 6
                    if code2 == 27:
                         code2 = 7
                    if code2 == 28:
                         code2 = 8
                    if code2 == 29:
                         code2 = 9
                    if code2 == 30:
                         code2 = 0
        if code4 == 9:
                        if code5 == 9:
                            if code6 == 9:
                                if code7 == 9:
                                    if code8 == 9:
                                        if code3 == 10:
                                            code3= (code3 - 1)
        if code3 > 9:
                    code4= (code4 + 1)
                    if code3 == 10:
                         code3 = 0
                    if code3 == 11:
                         code3 = 1
                    if code3 == 12:
                         code3 = 2
                    if code3 == 13:
                         code3 = 3
                    if code3 == 14:
                         code3 = 4
                    if code3 == 15:
                         code3 = 5
                    if code3 == 16:
                         code3 = 6
                    if code3 == 17:
                         code3 = 7
                    if code3 == 18:
                         code3 = 8
                    if code3 == 19:
                         code3 = 9
                    if code3 == 20:
                         code3 = 0
                    if code3 == 21:
                         code3 = 1
                    if code3 == 22:
                         code3 = 2
                    if code3 == 23:
                         code3 = 3
                    if code3 == 24:
                         code3 = 4
                    if code3 == 25:
                         code3 = 5
                    if code3 == 26:
                         code3 = 6
                    if code3 == 27:
                         code3 = 7
                    if code3 == 28:
                         code3 = 8
                    if code3 == 29:
                         code3 = 9
                    if code3 == 30:
                         code3 = 0
        if code4 == 10:
                        if code5 == 9:
                            if code6 == 9:
                                if code7 == 9:
                                    if code8 == 9:
                                        if code3 < 10:
                                            code3= (code3 - 1)
        if code4 > 10:
                    code5= (code5 + 1)
                    if code4 == 10:
                         code4 = 0
                    if code4 == 11:
                         code4 = 1
                    if code4 == 12:
                         code4 = 2
                    if code4 == 13:
                         code4 = 3
                    if code4 == 14:
                         code4 = 4
                    if code4 == 15:
                         code4 = 5
                    if code4 == 16:
                         code4 = 6
                    if code4 == 17:
                         code4 = 7
                    if code4 == 18:
                         code4 = 8
                    if code4 == 19:
                         code4 = 9
                    if code4 == 20:
                         code4 = 0
                    if code4 == 21:
                         code4 = 1
                    if code4 == 22:
                         code4 = 2
                    if code4 == 23:
                         code4 = 3
                    if code4 == 24:
                         code4 = 4
                    if code4 == 25:
                         code4 = 5
                    if code4 == 26:
                         code4 = 6
                    if code4 == 27:
                         code4 = 7
                    if code4 == 28:
                         code4 = 8
                    if code4 == 29:
                         code4 = 9
                    if code4 == 30:
                         code4 = 0
        if code6 == 9:
                        if code7 == 9:
                            if code8 == 9:
                                if code5 < 10:
                                    code5= (code5 - 1)
        if code5 > 10:
                    code6= (code6 + 1)
                    code5= 0
                    if code7 == 9:
                        if code8 == 9:
                            if code6 < 10:
                                code6= (code6 - 1)
        if code6 > 10:
                    code7= (code7 + 1)
                    code6= 0
                    if code8 == 9:
                        if code7 < 10:
                            code7= (code7 - 1)
        if code7 > 10:
                    code8= (code8 + 1)
                    code7= 0
                    if code8 < 10:
                        code8= (code8 - 1)

    panseisan = panseisan2

    screen.fill((100, 100, 255)) #RED, GREEN, BLUE
    mouse_x, mouse_y = pygame.mouse.get_pos()

    pygame.draw.rect(screen, (0, 230, 0), Rect(0, 370, 600, 600))
    pygame.draw.rect(screen, (195, 215, 140), Rect(260, 400, 90, 92.5))
    pygame.draw.circle(screen, (195, 215, 140), (255, 446), 46)
    pygame.draw.circle(screen, (195, 215, 140), (355, 446), 46)
    pygame.draw.rect(screen, (150, 170, 100), Rect(260, 400, 15, 50))
    pygame.draw.rect(screen, (150, 170, 100), Rect(295, 400, 15, 50))
    pygame.draw.rect(screen, (150, 170, 100), Rect(330, 400, 15, 50))
    pygame.draw.rect(screen, (0, 0, 0), Rect(10, 100, 200, 60))

    lcd2.update_col(col=6, code=code2)
    lcd3.update_col(col=5, code=code3)
    lcd4.update_col(col=4, code=code4)
    lcd5.update_col(col=3, code=code5)
    lcd6.update_col(col=2, code=code6)
    lcd7.update_col(col=1, code=code7)
    lcd8.update_col(col=0, code=code8)
        

    pygame.display.flip()
pygame.quit()