import pygame
from pygame.locals import *
from Path import *
import sys
from Board import *
from Button import *
# from menu.AI_Menu import *
# from menu.StartMenu import *
from menu import StartMenu
# from StartMenu import *
# from Board import *
import Board
from Label import *
import globals


class lose:
    def __init__(self):
        pygame.display.set_caption(" Game Over ")


# Initialise pygame and the window
pygame.init()

# ActMenu = "UNO"
# pygame.display.set_caption(" Game Over ")

screen = pygame.display.set_mode((1280,740))
# bg_img_path=getPath("UNO", "images","bg1.png")
# bg_img_path=getPath("images","BGs","play_bg.jpg")
# bg = pygame.image.load(bg_img_path)
# bg = pygame.image.load(f'images/BGs/bg_board.png').convert()
bg = pygame.image.load(f'images/BGs/game_over.jpeg') #.convert()
bg= pygame.transform.scale(bg,(1280,740))


# gameover_label = Label('Game over', (100, 100), 72, 'white')
# score_label = Label(f'Your score: {globals.score}',(495, 490), 60, 'black')
# score_label = Label(f'Your score: {globals.score}', (490, 420), 60, 'white')
# score_label = Label(f'Your score: {globals.score}', (960, 272), 56, 'black')
# ai1_score_label = Label(f'AI1 score: {globals.ai1score}', (110, 157), 46, 'black')
# ai2_score_label = Label(f'AI2 score: {globals.ai2score}', (110, 277), 46, 'black')
# ai3_score_label = Label(f'AI3 score: {globals.ai3score}', (110, 397), 46, 'black')
# gameover_label.draw(screen)
# # score_label.draw(screen)
# over = pygame.mixer.Sound('menu/ooh.mp3')
# over.play()
# print("over sound")
# yay = pygame.mixer.Sound('menu/Children_Yay_Sound_Effect.mp3')
# yay.play()


pygame.display.flip()


# Main loop of the game - checking for new events and rendering the window picture

def loseEndMenu(ActMenu,x1,x2,x3,x4):
    ActMenu = "Lose"
    over = pygame.mixer.Sound('menu/ooh.mp3')
    over.play()
    print("over sound")
    
    score_List = [x1,x2,x3,x4]

    #Creating the Buttons 
    if 0 not in score_List:
        ReplayButton = Button("restart", 90 ,585, 300, 100)
        MenuButton = Button("menu", 490 ,585, 300, 100)
        ExitButton = Button("exit", 890 ,585, 300, 100)
    else:
        ReplayButton = Button("restart", 90 ,560, 300, 100)
        # ReplayButton = Button("restart", 90 ,521, 300, 100)
        MenuButton = Button("menu", 490 ,560, 300, 100)
        ExitButton = Button("exit", 890 ,560, 300, 100)


    # ReplayButton = Button("restart", 90 ,575, 300, 100)
    # MenuButton = Button("menu", 490 ,575, 300, 100)
    # ExitButton = Button("exit", 890 ,575, 300, 100)

    score_label = Label(f'Your score: {x1}', (960, 272), 56, 'black')
    ai1_score_label = Label(f'AI1 score: {x2}', (110, 157), 46, 'black')
    ai2_score_label = Label(f'AI2 score: {x3}', (110, 277), 46, 'black')
    ai3_score_label = Label(f'AI3 score: {x4}', (110, 397), 46, 'black')

    No_Card_Label_1 = Label("All cards have been drawn",(450, 495), 46, 'black')
    No_Card_Label_2 = Label("No winner, Game Over! ",(484, 535), 46, 'black')
    # No_Card_Label_1 = Label("All cards have been drawn",(468, 500), 40, 'black')
    # No_Card_Label_2 = Label("No winner, Game Over! ",(496, 535), 40, 'black')
    

    if ActMenu=="Lose":

        loseMenu = lose()

        while(True):
            screen.blit(bg,(0,0))
            
            ReplayButton.draw_button(screen)
            MenuButton.draw_button(screen)
            ExitButton.draw_button(screen)

            # gameover_label.draw(screen)
            score_label.draw(screen)
            ai1_score_label.draw(screen)
            ai2_score_label.draw(screen)
            ai3_score_label.draw(screen)


            if 0 not in score_List:
                No_Card_Label_1.draw(screen)
                No_Card_Label_2.draw(screen)
            else:
                pass


            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    pygame.quit()
                    sys.exit()
                
                if(event.type == pygame.MOUSEMOTION):

                    spot = pygame.mouse.get_pos()

                    if( ReplayButton.rect.collidepoint(spot)):
                        print("pygame.mouse.get_pos()): ", pygame.mouse.get_pos())
                        print("ReplayButton.rect: ", ReplayButton.rect)
                        ReplayButton.set_hover(True)
                        ReplayButton.set_grey(screen)
                        
                    else : 
                        ReplayButton.set_hover(False)
                        ReplayButton.set_grey(screen)
                    
                    if( MenuButton.rect.collidepoint(spot)):
                        MenuButton.set_hover(True)
                        MenuButton.set_grey(screen)
                    else : 
                        MenuButton.set_hover(False)
                        MenuButton.set_grey(screen)
                    
                    if( ExitButton.rect.collidepoint(spot)):
                        ExitButton.set_hover(True)
                        ExitButton.set_grey(screen)
                    else : 
                        ExitButton.set_hover(False)
                        ExitButton.set_grey(screen) 
                
            
                if( event.type == pygame.MOUSEBUTTONDOWN):

                    spot = pygame.mouse.get_pos()
                
                    if( ReplayButton.rect.collidepoint(spot)):
                        ActMenu="PlayBoard"
                        Board.board(ActMenu) 
                        # board(ActMenu)


                    if( MenuButton.rect.collidepoint(spot)):
                        ActMenu ="MainMenu"
                        StartMenu.startMenu(ActMenu)
                        # startMenu(ActMenu)
                        # AIMenu(ActMenu)
                        
                    if (ExitButton.rect.collidepoint(pygame.mouse.get_pos())):
                        pygame.quit()
                        sys.exit()


            pygame.display.flip()
