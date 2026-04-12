# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the name of the character.

define mc = Character(_("Me"), color="#12da00")
define fw = Character(_("Flesh Walker"), color="#ac0404")

# This is a variable that is True if you've compared a VN to a book, and False otherwise.
default book = False

# Placeholder image to test how it works
image bg PlatinumLarge = im.Scale("bg PlatinumLarge.png", 1920, 1080)
# All background images going forward should be in 1920x1080 resolution.

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

    #show me

    # These display lines of dialogue.

    "You wake up with a sharp, pulsing ache across your lower torso. For a moment, you can't breathe. The cold floor presses against your cheek, and your vision swims as you try to remember where you are—or what happened."

    "When you manage to roll onto your back, you see the bandages first. A long, horizontal wrap stretches across your lower abdomen, tight and clean. Someone treated the wound. 
        Someone kept you alive. But you don’t remember who."

    "The room around you is dim, lit by a few flickering ceiling lights. Dust drifts lazily through the air. As your eyes adjust, you make out the cracked remains of a sign on the far wall:"

    mc "{b}CHARLESWOOD POLICE DEPARTMENT{/b}"

    "Most of the letters are missing or warped, but the meaning is clear enough. This was once a lobby. Now it feels abandoned—quiet in a way that doesn't feel natural."

    "You push yourself upright, unsteady. Your uniform is torn, scorched in places. The insignia on your shoulder—{b}Recon Unit{/b}—is still visible, though faded. 
        You remember the mission. You remember the boss. You remember pain."
    
    "Everything after that is blank."

    "You stagger forward, scanning the room. A collapsed desk. Scattered papers. A toppled chair. And then—another body."

    "A recon uniform, same as yours. Same insignia & gear. They're slumped against a wall, unmoving. You kneel beside them, checking for anything useful." 
    "Their equipment belt holds a {b}rifle{/b} with an empty chamber and a {b}sidearm{/b} with a single full magazine. You take both. Training, not instinct."

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
        
        #"Frozen Ghost Warehouse" :
            #jump frozen_Ghost_Warehouse
        
        #"Mutated Forest" :
            #jump mutated_Forest

        #"The Last City Ruins" :
            #jump the_Last_City_Ruins

        #"Alien Amusement Park" :
            #jump alien_Amusement_Park


    label alien_Town:
        #Scene changes to the outskirts of the Alien Town.
        "The tablet's signal leads you to the outskirts of a small settlement—if it can even be called that anymore.
        From a distance, the houses look almost cheerful, painted in bright colors that don't belong on Earth."

        "But the closer you get, the more wrong everything feels."

        "The air is warm. Too warm. And the wind is completely still."
        "Your tracker vibrates once."

        "{b}ALPHA-TEAM SIGNALS DETECTED — MULTIPLE SOURCES{/b}"

        "{b}All{/b} of them are somewhere inside the cornfield ahead. You tighten your grip on your rifle and step forward."

        # Change scene to cornfield
        # Not sure if there is supposed to be ambient sounds of birds and insects. Describing the sounds seems weird
        "The corn towers over you—far taller than it should be. The stalks sway gently, even though there's no breeze."
        "The stalks brush against your armor with a soft, rubbery texture. Not like plants. More like skin."

        "Your tracker pings again."
        "{b}ALPHA-5 — LAST POSITION: 42m{/b}"
        "You push deeper into the corn."

        # Maybe another scene change for the rustling cornfield? Or audio?
        "You take another step."
        "Something takes one with you."
        "You freeze."
        "The cornfield freezes with you."
        "Your tracker vibrates again—more urgently this time."
        "{b}ALPHA-5 — LAST POSITION: 18m{/b}"
        "You force yourself to keep moving."

        # Tightening cornfield path. Really feels like this should be a new scene but idk.
        "The deeper you go, the narrower the path becomes."
        "You try to push them aside. They bend too easily—like muscle, not plant fiber."

        "Your flashlight catches something on one of the stalks:"
        # Maybe a scene change here to reveal the blood
        "A smear of dried blood."
        "Human...You swallow hard and continue."

        # Scene changes and reveals a house
        # "Up close, the walls pulse faintly, like they’re breathing." -Not sure how pulsing walls are gonna look
        "Your tracker vibrates once."
        "{b}ALPHA-5 — LAST POSITION: 3m{/b}"

        mc "This is the place."
        # Scene changes to the inside of the house I guess?
        "You step inside"
        "The air is warm and humid. The walls bulge slightly, as if something beneath them shifts when you're not looking." #Again, not sure if animiated background is possible
        "Your flashlight beam catches something on the floor:"
        "A rifle. A torn glove. A smear of blood leading toward a back room." # This could be edited to be interactible I think, but I can't implement this right now.

        "You follow the blood trail."

        #Scene change again:
        "The room is empty—except for a single boot lying in the center of the floor. The floor beneath it bulges upward in a human-shaped outline, frozen mid-struggle."
        #"The walls around the outline are stretched, as if something inside them pushed outward before being pulled back in."
        #"A sidearm lies nearby, bent at an impossible angle."
        #The above 2 lines feel weird to narrate. IDK if it'll be possible to explain this just visually. Or if Jordan will have time.
        "This is where Alpha-5 died."

        "Your tracker pings again—another signal deeper in the town."
        "You leave quickly"

        # The cornfield comes back, and then transitions to revealing an identical house, just different colors to the previous one
        "Your tracker vibrates violently."
        "{b}ALPHA-7 — LAST POSITION: 0m{/b}"
        # Another interior. Recolor previous ones I guess?
        "You step inside."
        "{b}*BAM!!!*{/B}" #Or use audio
        "The door slams shut behind you."
        # "The walls ripple." Probably not possible to show.

        "Something moves under the floorboards." #Add SFX
        # "Your flashlight flickers, then stabilizes." This might be visually represented? Maybe
        "On the floor lies a cracked helmet marked: {b}ALPHA-7{/b}"
        "Next to it, half-melted into the fleshy floor, is a small recording device."
        "You pry it free."
        "It crackles to life."
        "You've recovered Alpha-7's log." #Can change how to represent this later.
        "As you continue to explore the house, you find subtle signs of Alpha-3's struggle."

        # Scene changes to show the backdoor.
        # The rear doorframe is shattered outward.
        # Deep gouges—human fingernails—run across the surface.
        # Description of the door frame can just be visual

        "A broken comms unit lies on the floor, still displaying:"
        "{b}ALPHA-3 — SIGNAL LOST{/b}" #This could be visually displayed too...

        # "The floor near the door is warped, as if something heavy dragged across it." (This could just be visually displayed. Or kept in text.)
        "One section of wall is torn open from the inside. The edges pulse faintly, trying to close."
        # Cut to a new background showing the soldier uniform in the wall
        "Inside the tear, you see a scrap of fabric—Alpha‑3’s uniform color."
        "He tried to escape."
        "He didn't make it."

        "As you turn to leave, the house shifts."
        #Change scene to creepy door
        "Something opened the door as if expecting you to follow it."
        #"Looking out the window, you notice it is going to be night soon as the streetlights light a pathway towards the church which is incredibly well lit." This can just be shown with lighting the in background
        menu:
            "Stay in the house":
                jump flesh_Walker_End
            "Make a run for it":
                jump flesh_Walker_End
            "Go to the Church":
                jump flesh_Walker_Boss

    label frozen_Ghost_Warehouse:
    label mutated_Forest:
    label the_Last_City_Ruins:
    label alien_Amusement_Park:
    label secret_Area:
    
    label flesh_Walker_End:
        #Scene changes to night time cornfield
        "You can hear the creature catching up to you at a rapid speed."
        "You pull out your pistol and put a couple of rounds down into the cornfield behind you to no avail."
        "Continue sprinting, you can feel the exhaustion. You are running out of breath. With no bearings where you are. You slow down and start to listen."
        # Only breath sounds

        "Has the monster moved on? No. It's here."
        #Footstep audio
        "You suddenly hear footsteps from {b}behind{/b}."
        "You turn and fire your rifle, emptying the magazine." #Insert 30 seconds of nonstop full auto until a click sound.

        mc "Shit!"
        "You're out of ammo."

        "You here it next to you, breathing down your neck and before you can react you can only hear the crunch of your ribs."

        "You escape into a house and barricade all the doors."
        "You turn a table over and point your rifle at the only entrance to the house."
        "You can hear it rounding the house, as if cornering its prey." #Not sure how the audio is going to go
        "You grip the rifle tight in your hand trying to not recall what had happened to Alpha 7."
        "Then the rounding sound stopped, and the only sound you can hear is the sound of your own breath." #Play appropriate audio
        fw "...I'm inside now. Walls feel closer. Something's moving under the floor. I think it knows I'm here."
        "Before you can react, a pair of sharp claws impales your chest and dragged you though the window."
        "You swore was a wall when you barricaded yourself in."

    label flesh_Walker_Boss:
        
    label death:
        "{b}You Died{/b}"
        return
        
    # This ends the game.

    return
