# -----------------------------------------------------------------------
# Character definitions
# -----------------------------------------------------------------------

define red_char  = Character("First Character",  color="#FF0000")
define blue_char = Character("Second Character", color="#0000FF")
define green_char  = Character("Third Character",  color="#00FF00")


# -----------------------------------------------------------------------
# Game code
# -----------------------------------------------------------------------

# Initial game label must be 'start'.
label start:

    # Ren'py auto-reads from other files in the directory.
    call chapter_one

    return
