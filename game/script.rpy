# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the name of the character.

define m = Character(_("Me"), color="#fb2222")

# This is a variable that is True if you've compared a VN to a book, and False otherwise.
default book = False

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # Start by playing some music.
    # play music "illurock.opus"

    scene bg room
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show me

    # These display lines of dialogue.

    m "Placeholders."

    m "placeholders 2"

    "{b}Bad Ending{/b}."
        
    # This ends the game.

    return
