# -----------------------------------------------------------------------
# Character definitions
# -----------------------------------------------------------------------

define sha = Character("Shana",  color="#FF0000")
define hai = Character("Hailey", color="#0000FF")

# -----------------------------------------------------------------------
# Game code
# -----------------------------------------------------------------------

# Initial game label must be 'start'.
label start:

    # Ren'py auto-reads from other files in the directory.
    call scene_one
    call scene_two
    call scene_three

    return
