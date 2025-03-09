import sys
import pygame
from pygame.locals import Rect
from LCD_font import LCD_font_styles
from LCD_font import LCD_font
from pygame.locals import *

def DisplayPanNum(pannnokazu):
     lcd2.update_col(col=6, code=pannnokazu%10)
     lcd3.update_col(col=5, code=pannnokazu/10%10)
     lcd4.update_col(col=4, code=pannnokazu/100%10)
     lcd5.update_col(col=3, code=pannnokazu/1000%10)
     lcd6.update_col(col=2, code=pannnokazu/10000%10)
     lcd7.update_col(col=1, code=pannnokazu/100000%10)
     lcd8.update_col(col=0, code=pannnokazu/1000000%10)

def DisplayMochiGaneNum(code14):
    lcd14.update_col(col=9, code=code14%10)
    lcd15.update_col(col=8, code=code14/10%10)
    lcd16.update_col(col=7, code=code14/100%10)
    lcd17.update_col(col=6, code=code14/1000%10)
    lcd18.update_col(col=5, code=code14/10000%10)
    lcd19.update_col(col=4, code=code14/100000%10)
    lcd20.update_col(col=3, code=code14/1000000%10)
    lcd21.update_col(col=2, code=code14/10000000%10)
    lcd22.update_col(col=1, code=code14/100000000%10)
    lcd23.update_col(col=0, code=code14/1000000000%10)

def DisplaySeisanKaneNum(panseisankane):
    if panseisanurikire == 0:
        lcd26.update_col(col=6, code=panseisankane%10)
        lcd27.update_col(col=5, code=panseisankane/10%10)
        lcd28.update_col(col=4, code=panseisankane/100%10)
        lcd29.update_col(col=3, code=panseisankane/1000%10)
        lcd30.update_col(col=2, code=panseisankane/10000%10)
        lcd31.update_col(col=1, code=panseisankane/100000%10)
        lcd32.update_col(col=0, code=panseisankane/1000000%10)
    if panseisanurikire == 1:
        lcd26.update_col(col=0, code=39)
        lcd27.update_col(col=1, code=40)
        lcd28.update_col(col=2, code=41)
        lcd29.update_col(col=3, code=42)
        lcd30.update_col(col=4, code=40)
        lcd31.update_col(col=5, code=43)
        lcd32.update_col(col=6, code=44)

def DisplayUrineKaneNum(urinekane):
    if urineurikire == 0:
        lcd36.update_col(col=6, code=urinekane%10)
        lcd37.update_col(col=5, code=urinekane/10%10)
        lcd38.update_col(col=4, code=urinekane/100%10)
        lcd39.update_col(col=3, code=urinekane/1000%10)
        lcd40.update_col(col=2, code=urinekane/10000%10)
        lcd41.update_col(col=1, code=urinekane/100000%10)
        lcd42.update_col(col=0, code=urinekane/1000000%10)
    if urineurikire == 1:
        lcd36.update_col(col=0, code=39)
        lcd37.update_col(col=1, code=40)
        lcd38.update_col(col=2, code=41)
        lcd39.update_col(col=3, code=42)
        lcd40.update_col(col=4, code=40)
        lcd41.update_col(col=5, code=43)
        lcd42.update_col(col=6, code=44)

def DisplayTorofiKaneNum(torofikane):
    if torofiurikire == 0:
        lcd43.update_col(col=9, code=torofikane%10)
        lcd44.update_col(col=8, code=torofikane/10%10)
        lcd45.update_col(col=7, code=torofikane/100%10)
        lcd46.update_col(col=6, code=torofikane/1000%10)
        lcd47.update_col(col=5, code=torofikane/10000%10)
        lcd48.update_col(col=4, code=torofikane/100000%10)
        lcd49.update_col(col=3, code=torofikane/1000000%10)
        lcd50.update_col(col=2, code=torofikane/10000000%10)
        lcd51.update_col(col=1, code=torofikane/100000000%10)
        lcd52.update_col(col=0, code=torofikane/1000000000%10)
    if torofiurikire == 1:
        lcd53.update_col(col=0, code=39)
        lcd54.update_col(col=1, code=40)
        lcd55.update_col(col=2, code=41)
        lcd56.update_col(col=3, code=42)
        lcd57.update_col(col=4, code=40)
        lcd58.update_col(col=5, code=43)
        lcd59.update_col(col=6, code=44)
    
    lcd33.update_col(col=2, code=code27)
    lcd34.update_col(col=1, code=code28)
    lcd35.update_col(col=0, code=code29)




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
ORIZINARU = (0, 230, 0)

LCD = LCD_font_styles
screen = pygame.display.set_mode([600, 600])
pygame.display.set_caption("pan clikker")
mouse_x, mouse_y = pygame.mouse.get_pos()
panseisan = 1
panseisankane = 50
panseisanhyouzi = 0
koeta = 0
zikan = 2
kieru = 0
pannnokazu = 1000000
kanenoryou = 5
panseisanurikire = 0
urinekane = 50
urineurikire = 0
urinehyouzi = 0
torofiurikire = 0
torofikane = 9999999999
torofi = 0
torofihyouzi = 0

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

lcd9 = LCD_font(screen)
lcd9.init_col(BLOCK_SIZE=8, BLOCK_INTV=8, COLOR_ON=WHITE, COLOR_OFF=BLACK)
lcd9.init_row(X_ORG=2, Y_ORG=12.75, COL_INTV=6)

lcd10 = LCD_font(screen)
lcd10.init_col(BLOCK_SIZE=8, BLOCK_INTV=8, COLOR_ON=WHITE, COLOR_OFF=BLACK)
lcd10.init_row(X_ORG=2, Y_ORG=12.75, COL_INTV=6)

lcd11 = LCD_font(screen)
lcd11.init_col(BLOCK_SIZE=8, BLOCK_INTV=8, COLOR_ON=WHITE, COLOR_OFF=BLACK)
lcd11.init_row(X_ORG=2, Y_ORG=12.75, COL_INTV=6)

lcd12 = LCD_font(screen)
lcd12.init_col(BLOCK_SIZE=8, BLOCK_INTV=8, COLOR_ON=WHITE, COLOR_OFF=BLACK)
lcd12.init_row(X_ORG=2, Y_ORG=12.75, COL_INTV=6)

lcd13 = LCD_font(screen)
lcd13.init_col(BLOCK_SIZE=8, BLOCK_INTV=8, COLOR_ON=WHITE, COLOR_OFF=BLACK)
lcd13.init_row(X_ORG=2, Y_ORG=12.75, COL_INTV=6)

lcd14 = LCD_font(screen)
lcd14.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=BLACK, COLOR_OFF=ORIZINARU)
lcd14.init_row(X_ORG=13, Y_ORG=65, COL_INTV=6)

lcd15 = LCD_font(screen)
lcd15.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=BLACK, COLOR_OFF=ORIZINARU)
lcd15.init_row(X_ORG=13, Y_ORG=65, COL_INTV=6)

lcd16 = LCD_font(screen)
lcd16.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=BLACK, COLOR_OFF=ORIZINARU)
lcd16.init_row(X_ORG=13, Y_ORG=65, COL_INTV=6)

lcd17 = LCD_font(screen)
lcd17.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=BLACK, COLOR_OFF=ORIZINARU)
lcd17.init_row(X_ORG=13, Y_ORG=65, COL_INTV=6)

lcd18 = LCD_font(screen)
lcd18.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=BLACK, COLOR_OFF=ORIZINARU)
lcd18.init_row(X_ORG=13, Y_ORG=65, COL_INTV=6)

lcd19 = LCD_font(screen)
lcd19.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=BLACK, COLOR_OFF=ORIZINARU)
lcd19.init_row(X_ORG=13, Y_ORG=65, COL_INTV=6)

lcd20 = LCD_font(screen)
lcd20.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=BLACK, COLOR_OFF=ORIZINARU)
lcd20.init_row(X_ORG=13, Y_ORG=65, COL_INTV=6)

lcd21 = LCD_font(screen)
lcd21.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=BLACK, COLOR_OFF=ORIZINARU)
lcd21.init_row(X_ORG=13, Y_ORG=65, COL_INTV=6)

lcd22 = LCD_font(screen)
lcd22.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=BLACK, COLOR_OFF=ORIZINARU)
lcd22.init_row(X_ORG=13, Y_ORG=65, COL_INTV=6)

lcd23 = LCD_font(screen)
lcd23.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=BLACK, COLOR_OFF=ORIZINARU)
lcd23.init_row(X_ORG=13, Y_ORG=65, COL_INTV=6)

lcd24 = LCD_font(screen)
lcd24.init_col(BLOCK_SIZE=8, BLOCK_INTV=8, COLOR_ON=WHITE, COLOR_OFF=BLACK)
lcd24.init_row(X_ORG=55, Y_ORG=2, COL_INTV=6)

lcd25 = LCD_font(screen)
lcd25.init_col(BLOCK_SIZE=8, BLOCK_INTV=8, COLOR_ON=WHITE, COLOR_OFF=BLACK)
lcd25.init_row(X_ORG=54, Y_ORG=2, COL_INTV=6)

lcd26 = LCD_font(screen)
lcd26.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=BLACK, COLOR_OFF=BLUE)
lcd26.init_row(X_ORG=33, Y_ORG=13, COL_INTV=6)

lcd27 = LCD_font(screen)
lcd27.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=BLACK, COLOR_OFF=BLUE)
lcd27.init_row(X_ORG=33, Y_ORG=13, COL_INTV=6)

lcd28 = LCD_font(screen)
lcd28.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=BLACK, COLOR_OFF=BLUE)
lcd28.init_row(X_ORG=33, Y_ORG=13, COL_INTV=6)

lcd29 = LCD_font(screen)
lcd29.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=BLACK, COLOR_OFF=BLUE)
lcd29.init_row(X_ORG=33, Y_ORG=13, COL_INTV=6)

lcd30 = LCD_font(screen)
lcd30.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=BLACK, COLOR_OFF=BLUE)
lcd30.init_row(X_ORG=33, Y_ORG=13, COL_INTV=6)

lcd31 = LCD_font(screen)
lcd31.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=BLACK, COLOR_OFF=BLUE)
lcd31.init_row(X_ORG=33, Y_ORG=13, COL_INTV=6)

lcd32 = LCD_font(screen)
lcd32.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=BLACK, COLOR_OFF=BLUE)
lcd32.init_row(X_ORG=33, Y_ORG=13, COL_INTV=6)

lcd33 = LCD_font(screen)
lcd33.init_col(BLOCK_SIZE=8, BLOCK_INTV=8, COLOR_ON=WHITE, COLOR_OFF=BLACK)
lcd33.init_row(X_ORG=8, Y_ORG=21.5, COL_INTV=6)

lcd34 = LCD_font(screen)
lcd34.init_col(BLOCK_SIZE=8, BLOCK_INTV=8, COLOR_ON=WHITE, COLOR_OFF=BLACK)
lcd34.init_row(X_ORG=8, Y_ORG=21.5, COL_INTV=6)

lcd35 = LCD_font(screen)
lcd35.init_col(BLOCK_SIZE=8, BLOCK_INTV=8, COLOR_ON=WHITE, COLOR_OFF=BLACK)
lcd35.init_row(X_ORG=8, Y_ORG=21.5, COL_INTV=6)

lcd36 = LCD_font(screen)
lcd36.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=BLACK, COLOR_OFF=BLUE)
lcd36.init_row(X_ORG=33, Y_ORG=22, COL_INTV=6)

lcd37 = LCD_font(screen)
lcd37.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=BLACK, COLOR_OFF=BLUE)
lcd37.init_row(X_ORG=33, Y_ORG=22, COL_INTV=6)

lcd38 = LCD_font(screen)
lcd38.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=BLACK, COLOR_OFF=BLUE)
lcd38.init_row(X_ORG=33, Y_ORG=22, COL_INTV=6)

lcd39 = LCD_font(screen)
lcd39.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=BLACK, COLOR_OFF=BLUE)
lcd39.init_row(X_ORG=33, Y_ORG=22, COL_INTV=6)

lcd40 = LCD_font(screen)
lcd40.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=BLACK, COLOR_OFF=BLUE)
lcd40.init_row(X_ORG=33, Y_ORG=22, COL_INTV=6)

lcd41 = LCD_font(screen)
lcd41.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=BLACK, COLOR_OFF=BLUE)
lcd41.init_row(X_ORG=33, Y_ORG=22, COL_INTV=6)

lcd42 = LCD_font(screen)
lcd42.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=BLACK, COLOR_OFF=BLUE)
lcd42.init_row(X_ORG=33, Y_ORG=22, COL_INTV=6)

lcd43 = LCD_font(screen)
lcd43.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=BLACK, COLOR_OFF=BLUE)
lcd43.init_row(X_ORG=15, Y_ORG=38, COL_INTV=6)

lcd44 = LCD_font(screen)
lcd44.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=BLACK, COLOR_OFF=BLUE)
lcd44.init_row(X_ORG=15, Y_ORG=38, COL_INTV=6)

lcd45 = LCD_font(screen)
lcd45.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=BLACK, COLOR_OFF=BLUE)
lcd45.init_row(X_ORG=15, Y_ORG=38, COL_INTV=6)

lcd46 = LCD_font(screen)
lcd46.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=BLACK, COLOR_OFF=BLUE)
lcd46.init_row(X_ORG=15, Y_ORG=38, COL_INTV=6)

lcd47 = LCD_font(screen)
lcd47.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=BLACK, COLOR_OFF=BLUE)
lcd47.init_row(X_ORG=15, Y_ORG=38, COL_INTV=6)

lcd48 = LCD_font(screen)
lcd48.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=BLACK, COLOR_OFF=BLUE)
lcd48.init_row(X_ORG=15, Y_ORG=38, COL_INTV=6)

lcd49 = LCD_font(screen)
lcd49.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=BLACK, COLOR_OFF=BLUE)
lcd49.init_row(X_ORG=15, Y_ORG=38, COL_INTV=6)

lcd50 = LCD_font(screen)
lcd50.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=BLACK, COLOR_OFF=BLUE)
lcd50.init_row(X_ORG=15, Y_ORG=38, COL_INTV=6)

lcd51 = LCD_font(screen)
lcd51.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=BLACK, COLOR_OFF=BLUE)
lcd51.init_row(X_ORG=15, Y_ORG=38, COL_INTV=6)

lcd52 = LCD_font(screen)
lcd52.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=BLACK, COLOR_OFF=BLUE)
lcd52.init_row(X_ORG=15, Y_ORG=38, COL_INTV=6)

lcd53 = LCD_font(screen)
lcd53.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=BLACK, COLOR_OFF=BLUE)
lcd53.init_row(X_ORG=20, Y_ORG=38, COL_INTV=6)

lcd54 = LCD_font(screen)
lcd54.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=BLACK, COLOR_OFF=BLUE)
lcd54.init_row(X_ORG=20, Y_ORG=38, COL_INTV=6)

lcd55 = LCD_font(screen)
lcd55.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=BLACK, COLOR_OFF=BLUE)
lcd55.init_row(X_ORG=20, Y_ORG=38, COL_INTV=6)

lcd56 = LCD_font(screen)
lcd56.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=BLACK, COLOR_OFF=BLUE)
lcd56.init_row(X_ORG=20, Y_ORG=38, COL_INTV=6)

lcd57 = LCD_font(screen)
lcd57.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=BLACK, COLOR_OFF=BLUE)
lcd57.init_row(X_ORG=20, Y_ORG=38, COL_INTV=6)

lcd58 = LCD_font(screen)
lcd58.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=BLACK, COLOR_OFF=BLUE)
lcd58.init_row(X_ORG=20, Y_ORG=38, COL_INTV=6)

lcd59 = LCD_font(screen)
lcd59.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=BLACK, COLOR_OFF=BLUE)
lcd59.init_row(X_ORG=20, Y_ORG=38, COL_INTV=6)

lcd60 = LCD_font(screen)
lcd60.init_col(BLOCK_SIZE=8, BLOCK_INTV=8, COLOR_ON=WHITE, COLOR_OFF=BLACK)
lcd60.init_row(X_ORG=5, Y_ORG=30, COL_INTV=6)

lcd61 = LCD_font(screen)
lcd61.init_col(BLOCK_SIZE=8, BLOCK_INTV=8, COLOR_ON=WHITE, COLOR_OFF=BLACK)
lcd61.init_row(X_ORG=5, Y_ORG=30, COL_INTV=6)

lcd62 = LCD_font(screen)
lcd62.init_col(BLOCK_SIZE=8, BLOCK_INTV=8, COLOR_ON=WHITE, COLOR_OFF=BLACK)
lcd62.init_row(X_ORG=5, Y_ORG=30, COL_INTV=6)

lcd63 = LCD_font(screen)
lcd63.init_col(BLOCK_SIZE=8, BLOCK_INTV=8, COLOR_ON=WHITE, COLOR_OFF=BLACK)
lcd63.init_row(X_ORG=5, Y_ORG=30, COL_INTV=6)

code9 = 31
code10 = 32
code11 = 33
code12 = 34
code13 = 35
code14 = 9999999999
code15 = 0
code16 = 0
code17 = 0
code18 = 0
code19 = 0
code20 = 0
code21 = 0
code22 = 0
code23 = 0
code24 = 36
code25 = 37
code26 = 38
code27 = 46
code28 = 45
code29 = 36
code30 = 47
code31 = 48
code32 = 49
code33 = 50


DisplayPanNum(pannnokazu)
DisplayMochiGaneNum(code14)
DisplaySeisanKaneNum(panseisankane)
DisplayUrineKaneNum(urinekane)
DisplayTorofiKaneNum(torofikane)

lcd24.update_col(col=0, code=code24)
lcd25.update_col(col=1, code=code25)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if not running:
            break
        
        if event.type == pygame.KEYDOWN:
            if pygame.K_SPACE:  # マウスが動いたとき
                mouse_x, mouse_y = pygame.mouse.get_pos()  # マウスの位置を取得
                print(f"マウスの位置: ({mouse_x}, {mouse_y})")

        # 作る！
        if mouse_x > 205 and mouse_x < 399 and mouse_y > 403 and mouse_y < 489:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pannnokazu= pannnokazu + panseisan

        # 売る！
        if mouse_x > 430 and mouse_x < 528 and mouse_y > 14 and mouse_y < 73:
            if event.type == MOUSEBUTTONDOWN:
                if pannnokazu > 0:
                    code14=  (code14 + kanenoryou * pannnokazu)
                    pannnokazu = 0
        # 生産力up！
        if mouse_x > 10 and mouse_x < 260 and mouse_y > 100 and mouse_y <160:
            if event.type == MOUSEBUTTONDOWN:
                if panseisan < 20 and code14 > (panseisankane - 1):
                        panseisan= panseisan + 1
                        code14= code14 - panseisankane
                        panseisankane= panseisankane * 1.5
        # 売値up！
        if mouse_x > 10 and mouse_x < 260 and mouse_y > 170 and mouse_y <230:
            if event.type == MOUSEBUTTONDOWN:
                if kanenoryou < 30 and code14 > (urinekane - 1):
                        kanenoryou= kanenoryou + 1
                        code14= code14 - urinekane
                        urinekane= urinekane * 1.5
        # トロフィ！
        if mouse_x > 10 and mouse_x < 260 and mouse_y > 240 and mouse_y <300:
            if event.type == MOUSEBUTTONDOWN:
                if torofi == 0 and code14 > (torofikane - 1):
                        torofi= 1
                        code14= code14 - torofikane                 
    if kanenoryou == 30:
        urineurikire = 1

    if panseisan == 20:
        panseisanurikire = 1

    if torofi == 1:
        torofiurikire = 1

    if mouse_x > 10 and mouse_x < 260 and mouse_y > 100 and mouse_y <160:
        panseisanhyouzi= 1
    else:
        panseisanhyouzi= 0

    if mouse_x > 10 and mouse_x < 260 and mouse_y > 170 and mouse_y <230:
        urinehyouzi= 1
    else:
        urinehyouzi= 0

    if mouse_x > 10 and mouse_x < 260 and mouse_y > 240 and mouse_y <300:
        torofihyouzi= 1
    else:
        torofihyouzi= 0


    screen.fill((100, 100, 255)) #RED, GREEN, BLUE
    mouse_x, mouse_y = pygame.mouse.get_pos()

    pygame.draw.rect(screen, (0, 230, 0), Rect(0, 370, 600, 600))

    # パン本体

    pygame.draw.rect(screen, (195, 215, 140), Rect(260, 400, 90, 92.5))
    pygame.draw.circle(screen, (195, 215, 140), (255, 446), 46)
    pygame.draw.circle(screen, (195, 215, 140), (355, 446), 46)
    pygame.draw.rect(screen, (150, 170, 100), Rect(260, 400, 15, 50))
    pygame.draw.rect(screen, (150, 170, 100), Rect(295, 400, 15, 50))
    pygame.draw.rect(screen, (150, 170, 100), Rect(330, 400, 15, 50))

    pygame.draw.rect(screen, (0, 0, 0), Rect(10, 100, 250, 60))
    pygame.draw.rect(screen, (0, 0, 0), Rect(430, 15, 100, 60))
    pygame.draw.rect(screen, (0, 0, 0), Rect(10, 170, 250, 60))
    pygame.draw.rect(screen, (0, 0, 0), Rect(10, 240, 250, 60))

    DisplayPanNum(pannnokazu)
    DisplayMochiGaneNum(code14)


    if panseisanhyouzi == 1:
        DisplaySeisanKaneNum(panseisankane)

    if urinehyouzi == 1:
        DisplayUrineKaneNum(urinekane)

    if torofihyouzi == 1:
        DisplayTorofiKaneNum(torofikane)


    lcd9.update_col(col=0, code=code9)
    lcd10.update_col(col=1, code=code10)
    lcd11.update_col(col=2, code=code11)
    lcd12.update_col(col=3, code=code12)
    lcd13.update_col(col=4, code=code13)

    lcd24.update_col(col=0, code=code24)
    lcd25.update_col(col=1, code=code25)

    lcd33.update_col(col=2, code=code27)
    lcd34.update_col(col=1, code=code28)
    lcd35.update_col(col=0, code=code29)

    lcd60.update_col(col=0, code=code30)
    lcd61.update_col(col=1, code=code31)
    lcd62.update_col(col=2, code=code32)
    lcd63.update_col(col=3, code=code33)
   
    pygame.display.flip()
pygame.quit()