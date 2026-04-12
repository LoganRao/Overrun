# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the name of the character.

define mc = Character(_("Me"), color="#fb2222")

# This is a variable that is True if you've compared a VN to a book, and False otherwise.
default book = False

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # Start by playing some music.
    play music "audio/On-Lyne  PARTY OF YOUR LIFETIME Instrumental  Technocyte Coda Menu Theme - OliveOil (youtube).mp3"


    scene bg PlatinumLarge
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show me

    # These display lines of dialogue.

    "You wake up with a sharp, pulsing ache across your lower torso. For a moment, you can’t breathe. The cold floor presses against your cheek, and your vision swims as you try to remember where you are—or what happened."

    "When you manage to roll onto your back, you see the bandages first. A long, horizontal wrap stretches across your lower abdomen, tight and clean. Someone treated the wound. 
        Someone kept you alive. But you don’t remember who."

    "The room around you is dim, lit by a few flickering ceiling lights. Dust drifts lazily through the air. As your eyes adjust, you make out the cracked remains of a sign on the far wall:"

    mc "{b}CHARLESWOOD POLICE DEPARTMENT{/b}"

    "Most of the letters are missing or warped, but the meaning is clear enough. This was once a lobby. Now it feels abandoned—quiet in a way that doesn’t feel natural."

    "You push yourself upright, unsteady. Your uniform is torn, scorched in places. The insignia on your shoulder—{b}Recon Unit{/b}—is still visible, though faded. 
        You remember the mission. You remember the boss. You remember pain."
    
    "Everything after that is blank."

    "You stagger forward, scanning the room. A collapsed desk. Scattered papers. A toppled chair. And then—another body."

    "A recon uniform, same as yours. Same insignia & gear. They’re slumped against a wall, unmoving. You kneel beside them, checking for anything useful." 
    "Their equipment belt holds a {b}rifle{/b} with an empty chamber and a {b}}sidearm{/b} with a single full magazine. You take both. Training, not instinct."

    "As you search further, you find something tucked beneath their arm:"
    "A {b}tablet{/b}, cracked but still functional."

    "When you power it on, the screen flickers to life. A simple interface appears—clean, minimal, unmistakably military. One option is highlighted."

    # Transition to the tablet screen
    # Add audio effects
    
    # If there is a transition that leads to the pop up to explore other areas that'd be great.
    # Couldn't find anything like that so I don't know if it even exists.

    "Choose an area to explore:"
    menu:
        "Alien Town" :
            jump alien_Town
        
        "Frozen Ghost Warehouse" :
            jump frozen_Ghost_Warehouse
        
        "Mutated Forest" :
            jump mutated_Forest

        "The Last City Ruins" :
            jump the_Last_City_Ruins

        "Alien Amusement Park" :
            jump alien_Amusement_Park


    label alien_Town:

    label frozen_Ghost_Warehouse:
    label mutated_Forest:
    label the_Last_City_Ruins:
    label alien_Amusement_Park:
    label secret_Area:


    "{b}The End{/b}."
        
    # This ends the game.

    return
