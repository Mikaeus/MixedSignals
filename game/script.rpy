# -----------------------------------------------------------------------
# Character definitions
# -----------------------------------------------------------------------

define sha = Character("Shana",  color="#00FF00")
define hai = Character("Hailey", color="#FF0000")

# -----------------------------------------------------------------------
# Variable definitions
# -----------------------------------------------------------------------

#default reassurance = ""

# -----------------------------------------------------------------------
# Game code
# -----------------------------------------------------------------------

# Initial game label must be 'start'.
# Ren'py auto-reads from other files in the directory.
label start:

    call scene_one_hailey

    #"Cue POV switch -- scene one."

    call scene_one_shana

    #call scene_two_hailey
    #call scene_two_shana

    #call scene_three_hailey
    #call scene_three_shana

    return
