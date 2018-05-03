# -----------------------------------------------------------------------
# Game code
# -----------------------------------------------------------------------

# Initial game label must be 'start'
label chapter_one:

    # Enter Red Character
    show red at left
    red_char  "Hello, I'm a red cube."
    red_char  "I'm slightly obscured by the text box."
    
    show red at center with move
    red_char  "As you can see, I can slide right, but not up."
    hide red
    
    # Enter blue character
    show blue normal at right
    blue_char "Heya! I'm a blue cube!"
    blue_char "I'm also behind the text box!"
    
    show blue at center
    blue_char "I can't teleport up, but I'm great at teleporting left!"
    hide blue
    
    # Enter green character
    show green
    green_char "I am the green cube. The most powerful of the cube family."
    
    menu:
        green_char "Do you believe me?"
        
        "I think you're a weakling, green cube!":
            $ angry_green = True

        "Oh, great green cube, I believe! I believe!":
            $ angry_green = False
        
label chapter_one_after_menu:
    if angry_green == True:
        show green angry
        green_char "Fool! How dare you insult me!"
        green_char "I will demonstrate my power by levitating upward."
        show green angry at Position(xpos = 0.5, xanchor=0.5, ypos=0.5, yanchor=0.5) with move

    if angry_green == False:
        show green happy
        green_char "Ohoho! You're too kind, my dear."
        green_char "Just for you, I will demonstrate my levitation power."
        show green happy at Position(xpos = 0.5, xanchor=0.5, ypos=0.5, yanchor=0.5) with move
        
    green_char "Behold my power!"