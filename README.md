Rules Introduction (Game Logic) : 

    1. Card Logic: Only two values are given to the card class: color and number. Instead of using class inheritance class, use special numbers over ten to represent function cards:
                    card.number==11:reverseCard
                    card.number==12:take2Card
                    card.number==13:skipcard
                    card.number==14:wildCard
                    card.number==15:wild4Card
    
    2. AI Logic: 

Individual Tasks: 

    Shuming Shi: （ROLE: Leader）
        Responsible Modlues: all menus(Start Menu, Win End Menu, Lose End Menu, AI menu), 
                 Buttons, Path, Resize, change Color, discarded Pile, globals; help some with others'visualization(like AI_class...)
        Task Introduction:
            1. implement MEMU visualization things:  
                a. for StartMenu, add one Button(Start Button) to go into the Playboard screen;
                    # initially, we have three Buttons(Start, Menu, Exit):
                        click "Start": to get into the game board directly; 
                        click "Menu" to get into the AI Menu(3 Buttons: 1 player, 2 player, 3 player)
                           , which is prepared for user to choose different number of AI player
                           (Coz time is limited, we didn't finish it; so delete this module later); 
                        click "Exit" to exit the Game; 
                # b. for AImenu : 3 buttons(AI1,AI2, AI3)
                c. for WinEndMenu, show marks of AI players and Human player; 
                                   Add 3 buttons: Replay(back to game borad),
                                                  Menu(back to StartMenu), 
                                                  Exit(to exit this game)
                d. for LoseEndMenu, 3 buttons and show 4 players'scores(Same with WinEndMenu);
                                    Add Tips when the GameOver because there no card remain in the draw deck,
                                    & change the position of 3 buttons at the same time; 
            2. Buttons: def a bt_Resize() Function: can batch process images, to resize large number of button bg_images
                                                    , instead of using PS to resize img(to save time);
                        def draw Button Function: to draw the resized Buttons to current screen;
                        def set_hover() & get_hover() Function: REFERENCE (https://github.com/Medelouali/UNO-clone.git)
                        def set_grey() Function: when mouse hover on our buttons, the button will turns Grey(Actually is to change the button's 
                                                 bg imgs to grey one ---- images/buttons/blue/* --> ./grey/*)
            3. Path:  to help getPath in a more simplier way
            4. Resize: similar to bt_Resize Func, can batch process images: to Resize large number of images(like card imgs)
            5. change Color: show 4 color buttons to be selected, 
                             and draw a "current color Label" to the playboard screen as a tip(parameter is current color)
                             Change Color Logic: 
                                - ONLY when the player discard Wild Card, can the button be clicked, and change current color
                                  , update the "current color Label" in Game Borad simultaneously
                                  , if player didn't choose one color after he/she discard the wild cards
                                  , this player will be not able to discard the next card;
                                
                                - IF player discard other cards, but click the change color buttons, it will happend nothing
                                  , the current color won't be changed (in case someone may click these color buttons by mistake during UNO Game); 
            5. # discarded pile: to draw and show the area of discarded deck(draw a empty card to the screen to show the discarded deck area);
            6. globals: store global variavles;                  
            7. help others during free time
            8. design and draw menus' background images by iPad 


    JIEKE:
            playeract.py:
                playeractstep1:For the start of the game, the player designates a starting card
                playeractstep2:Used to judge various top cards as the game progresses, to limit the selection of which cards players can play, and to give feedback on the function of the cards to the next player
                specialcardturn：It is used to operate on the player during the game for the function cards played by the various upper deck cards.
    
            whosturn.py:Used to calculate the direction of play and the next player while the game is in progress, and finally feed the value to “whichplayer” for the index of “playerlist”  
    
            changecard.py:At the beginning of a player's turn, choose a discarded card from the hand and get a card from the draw pile
    
            AI_class.py.specialplay:Similar to playeract.py.specialcardturn 
    
    Song Li:
            AI class implements all the functions of basic AI, including: AI can independently touch cards, judge which cards can be played according to the top of the discard pile and the cards in hand, put the cards that can be played into a list, and select cards from this list at random. If the cards on the top of the pile are wildcard and wild4card, AI will also randomly select the color of the next player's cards, and AI class also calls draw_ The back function draws the hands of the top, left and right AI players. When the number of AI players' hands is greater than 7, the hands are displayed in the second row.
    
            Check_ uno_ The button class realizes drawing the UNO button and detecting the click position of the player's mouse. If the player does not click the UNO button when there is only one card in his hand, he will be punished by touching four cards. 
            
    Hui Guo:
    				The card class is implemented,including different types of cards and their attributes for logical judgment when playing cards, and the draw card method is provided to display images on the interface. Provides a method for judging the area of the card clicked by the mouse, which is used for judging when the card is played.
    				card painting: I found the card picture in one project(https://github.com/Medelouali/UNO-clone) and then I added Nottingham elements as the background with ps.
    				The card pile class is created, including the method for the player to deal cards, and the discard pile And the realization of the function and interface of displaying the top card of the deck and store the cards which have been played.
    				
    				The player class is created, with a method interface for drawing cards, and two methods and interface implementations for displaying cards based on the number of cards in the hand. A method for changing the order of cards is created, but in this game we use other judgment cards playing sequential method
    				
    				For the reference, https://www.youtube.com/watch?v=7BXDcBfk-04, This is a video about how to make an uno game, although it is not a visual game, and it is not object-oriented coding. But after watching the video, I have a clear understanding of the complete uno process and what work I need to do.
    				I found the card picture in this project: https://github.com/Medelouali/UNO-clone, and then I added Nottingham elements as the background with ps.


​    		
​    
​    

