# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the name of the character.

define mc = Character(_("Me"), color="#12da00")
define a7 = Character(_("Alpha-7"), color="#3f99ff")
define a4 = Character(_("Alpha-4"), color="#263cff")
define a8 = Character(_("Alpha-8"), color="#263cff")
define a10 = Character(_("Alpha-10"), color="#263cff")
define fw = Character(_("Flesh Walker"), color="#ac0404")

# This is a variable that is True if you've compared a VN to a book, and False otherwise.
default book = False
# Progression tracking
default areas_cleared = []          # list: "alpha_537", "alpha_4810", "alpha_11", "alpha_12", "alpha_9"
default escape_endings_count = 0    # int: 0–5 (triggers secret ending unlock at 5)

# Alpha-11 companion state
default alpha11_companion = False   # bool
default alpha11_abandoned = False   # bool
default alpha11_infection_pct = 0   # int: 10, 50, 75, 100

# Player resource flags
default has_medication = True       # bool: False if player visited Alpha-11 forest area first
default citrus_file_read = False    # bool: unlocks dialogue in secret ending
default has_lucky_charm = False     # bool: taken from Alpha-9 body

# Boss outcomes
default flesh_walker_dead = False
default frost_beast_dead = False
default sandworm_dead = False
default alpha9_dead = False
default alpha11_infected_dead = False
default dr_haze_defeated = False

default used_areas = {
    "alien_town": False,
    "alien_amusement_park": False,
    "secret_outpost": False,
    "frozen_warehouse": False,
    "city_ruins": False,
    "mutated_forest": False
}

# Secret ending stars (one per escape ending completed)
default star_count = 0              # int: 0–6

# Equipment
default rifle_ammo = False
default sidearm_ammo = True
default grenade = True

# For Alien town area
default boss_points = 0

# Track used choices
default used_cover = False
default used_run = False
default used_rifle = False
default used_sidearm = False
default used_grenade = False



# Placeholder image to test how it works
image bg PoliceDepartment = im.Scale("bg PoliceDepartment.png", 1920, 1080)
image bg AlienTown = im.Scale("bg AlienTown.png", 1920, 1080)
# All background images going forward should be in 1920x1080 resolution.

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # Start by playing some music.
    # play music "audio/On-Lyne  PARTY OF YOUR LIFETIME Instrumental  Technocyte Coda Menu Theme - OliveOil (youtube).mp3"
    scene bg PoliceDepartment
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    #show me

    "You wake up with a sharp, pulsing ache across your lower torso. For a moment, you can't breathe. The cold floor presses against your cheek, and your vision swims as you try to remember where you are—or what happened."

    "When you manage to roll onto your back, you see the bandages first. A long, horizontal wrap stretches across your lower abdomen, tight and clean. Someone treated the wound. 
        Someone kept you alive. But you don't remember who."

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
    jump area_menu

    label area_menu:
        # prob should have it's own background (or something)
        scene bg PoliceDepartment
        with fade
        menu:
            # Does not open up others
            "Explore Alien Town" if not used_areas["alien_town"]:
                $ used_areas["alien_town"] = True
                jump alien_town  

            # Opens up ruins
            "Explore Frozen Warehouse" if not used_areas["frozen_warehouse"]:
                $ used_areas["frozen_warehouse"] = True
                jump frozen_warehouse

            # Only used for demo
            "End of Demo" if (used_areas["frozen_warehouse"] and used_areas["alien_town"]):
                jump end_of_demo

            # # Opens up ruins
            # "Explore Mutated Forest (wip)" if not used_areas["mutated_forest"]:
            #     $ used_areas["mutated_forest"] = True
            #     jump mutated_forest          

            # # Opens up amusement park
            # "{color=#0000ffff}Explore City Ruins (wip){/color}" if (not used_areas["city_ruins"] and (used_areas["mutated_forest"] or used_areas["frozen_warehouse"])):
            #     $ used_areas["city_ruins"] = True
            #     jump city_ruins

            # # Does not open up others   
            # "Explore Alien Amusement Park (wip)" if (not used_areas["alien_amusement_park"] and used_areas["city_ruins"]):
            #     $ used_areas["alien_amusement_park"] = True
            #     jump alien_amusement_park

            # # Open from start, leads to different outcomes
            # "Explore Secret Outpost (wip)" if (not used_areas["secret_outpost"] and used_areas["alien_town"] and used_areas["alien_amusement_park"] and used_areas["frozen_warehouse"] and used_areas["city_ruins"] and used_areas["mutated_forest"]):
            #     $ used_areas["secret_outpost"] = True
            #     jump secret_outpost





        return

    # ─────────────────────────────────────────
    #  Alien Town
    # ─────────────────────────────────────────
    label alien_town:
        #Scene changes to the outskirts of the Alien Town.
        scene bg AlienTown
        with fade 

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
        # "Up close, the walls pulse faintly, like they're breathing." -Not sure how pulsing walls are gonna look
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
        
        #[BEGIN LOG]
        a7 "…Alpha-7… recording. I don't know how long I've got. The others… they're gone. Not dead. Just… gone."
        a7 "…we touched down near the town at dusk. Looked abandoned from a distance. Up close… The walls were warm. Like skin. It felt like the houses were listening to us breathe."
        a7 "Alpha‑3 ordered recon. Standard sweep. We split up to check the structures. Empty rooms, empty streets… but the air felt thick. Like the whole damn place was holding its breath."
        #[STATIC — LOW HUM]
        a7 "…movement in the cornfield. Something tall. Kept pace with us but never stepped into the light. Every time I turned, it froze."
        a7 "…first contact hit after nightfall. Fast. Invisible. Rounds didn't slow it. It didn't even try to kill us—just herded us deeper into the town like cattle."
        a7 "…Alpha‑5 went into one of the houses. The door slammed behind him. When we forced it open… the room wasn't the same. Warmer. Breathing. No sign of him."
        #[AUDIO DISTORTION — ORGANIC SHIFTING]
        a7 "…that's when I saw it. The thing in the corn. Flesh‑colored. Limbs like stretched muscle. It moved like it was part of the town… or the town was part of it."
        a7 "…it tore through the others. I ran. I don't know where they went. The houses shift when you're not looking. I swear I can hear them whispering under the floorboards."
        a7 "…I'm inside now. Walls feel closer. Something's moving under the floor. I think it knows I'm here."
        #[WEAPON CHAMBERING]
        a7 "…if anyone finds this… don't stay here. Don't touch the walls. And whatever you do… don't let the thing in the cornfield see you. Keep moving and get the hell out."
        #[UNINTELLIGIBLE ORGANIC SHIFTING — WET, LOW RUMBLE]
        a7 "…it's at the door…"
        # [GUNSHOTS — THEN SUDDEN SILENCE]
        # [VOICE RETURNS — WRONG, MIMICKED, MULTIPLE LAYERS]
        a7 "…if… you… out there… come… … your friends… are all… here…"
        a7 "…it's… a… worse fate… to be hunted… by… me…"
        # [STATIC — SIGNAL COLLAPSE]
        # [END LOG]

        #"You've recovered Alpha-7's log." #Can change how to represent this later.
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
        "Inside the tear, you see a scrap of fabric—Alpha‑3's uniform color."
        "He tried to escape."
        "He didn't make it."

        "As you turn to leave, the house shifts."
        #Change scene to creepy door
        "Something opened the door as if expecting you to follow it."
        #"Looking out the window, you notice it is going to be night soon as the streetlights light a pathway towards the church which is incredibly well lit." This can just be shown with lighting the in background

        jump round_1

        
    label round_1:
        call action_menu
        jump round_2

    label round_2:
        call action_menu
        jump round_3

    label round_3:
        call action_menu
        jump at_end_game

    # -------------------------
    # ACTION MENU (DYNAMIC)
    # -------------------------

    label action_menu:

        menu:

            "Look for cover in the house" if not used_cover:
                $ used_cover = True
                jump cover_result

            "Make a run for it" if not used_run:
                $ used_run = True
                jump run_result

            "Grab rifle and shoot" if not used_rifle:
                $ used_rifle = True
                jump rifle_check

            "Grab sidearm and shoot" if not used_sidearm:
                $ used_sidearm = True
                jump sidearm_check

            "Throw grenade" if not used_grenade:
                $ used_grenade = True
                jump grenade_check

        return

    # -------------------------
    # COVER
    # -------------------------

    label cover_result:
        $ boss_points -= 1
        "The enemy crushes your hiding spot, you barely jump out unscathed and reevaluate your options."
        return

    # -------------------------
    # RUN
    # -------------------------

    label run_result:
        $ boss_points += 1
        "Success, you escape the house, and look for the next step."
        return

    # -------------------------
    # RIFLE LOGIC
    # -------------------------

    label rifle_check:
        if rifle_ammo:
            jump rifle_success
        else:
            jump rifle_fail

    label rifle_success:
        $ boss_points += 2
        $ rifle_ammo = False
        "You use your rifle and fire at the enemy, dealing great damage to it"
        return

    label rifle_fail:
        $ boss_points -= 2
        "Your rifle is out of ammo and the enemy swipes during your confusion, you're still alive but injured."
        return

    # -------------------------
    # SIDEARM LOGIC
    # -------------------------

    label sidearm_check:
        if sidearm_ammo:
            jump sidearm_success
        else:
            jump sidearm_fail

    label sidearm_success:
        $ boss_points += 1
        $ sidearm_ammo = False
        "You succesfully shoot the enemy, it deals moderate damage, but it's still up and coming toward you"
        return

    label sidearm_fail:
        $ boss_points -= 1
        "The gun us empty, you jump back in the nick of time but it's nails scratch you"
        return

    # -------------------------
    # GRENADE LOGIC
    # -------------------------

    label grenade_check:
        if grenade:
            jump grenade_success
        else:
            jump grenade_fail

    label grenade_success:
        $ boss_points += 3
        $ grenade = False
        "You manage to land the hit, it does massive damage."
        return

    label grenade_fail:
        $ boss_points -= 3
        "You spend too much time looking for it and get clobbered to the floor, you get up and look for other options"
        return

    # -------------------------
    # ENDING
    # -------------------------

    label at_end_game:

        if boss_points >= 3:
            jump at_good_ending
        elif boss_points >= 0:
            jump at_neutral_ending
        else:
            jump at_bad_ending

    label at_good_ending:
        $ star_count += 1
        "You succeed in beating away the enemy. You decide to go back to the polic hub to recouperate and rethink your options."
        jump area_menu

    label at_neutral_ending:
        $ star_count += 1
        "You succesfully get away from the enemy, and go back to the police hub to recouperate"
        jump area_menu

    label at_bad_ending:
        $ used_cover = False
        $ used_run = False
        $ used_rifle = False
        $ used_sidearm = False
        $ used_grenade = False        
        "The enemy manages to catch you and {b}you die{/b}"

        "Return to start of area?"
        menu:
            "yes":
                jump alien_town
            "no":
                $ used_areas["alien_town"] = False
                jump area_menu

            
    
    # ─────────────────────────────────────────
    #  Frozen Ghost Warehouse
    # ─────────────────────────────────────────
    label frozen_warehouse:
        scene grey

        #Scene change to I think a town? We'll later change to the warehouse itself, but before that, not sure what it's supposed to be.
        "Your tablet lights up with multiple overlapping pings—{b}3 Alpha-team signatures{/b} clustered in the same location."
        "The signals are faint, flickering, as if something is interfering with them."

        "You follow the alleyway until it opens into a wide loading district."
        "That's when you see it."
        "A massive warehouse dominates the block, its metal walls coated in a thick layer of frost."
        "The surrounding pavement is frozen solid, cracked from the sudden temperature drop."

        "It looks like a blizzard hit this one building and nowhere else."
        "A cold mist rolls across the ground, curling around your boots."
        "Your breath fogs inside your helmet."

        # "The temperature drops another few degrees." This line feels unecessary

        #Scene changes to reveal the warehouse
        "The warehouse's main gate is secured with a heavy chain, but the metal is so brittle from the cold that it snaps apart the moment you strike it with your rifle's buttstock."
        "The gate groans as you push it open." #This could just be audio

        "Halfway through, the hinges crack. The entire gate collapses flat onto the frozen pavement with a metallic crash."
        "The sound echoes through the empty district." # Could use SFX here too.

        "Nothing answers."
        "You step inside the perimeter."

        "As you circle the warehouse, you notice something wrong with the loading dock door."
        "It's partially open—jammed halfway, as if something forced it upward and then stopped."
        "Frost clings to the edges of the metal, forming jagged crystalline teeth."
        "You approach slowly."
        "That's when you see it."
        "A body is wedged in the gap beneath the sliding door—cut cleanly in half by the weight of the frozen metal."
        "The torso is slumped outward, armor cracked and covered in frost."
        "The insignia on the shoulder is unmistakable: {b}ALPHA-4{/b}"

        "His outstretched hand is frozen to the concrete, fingers curled around a small recording device." #Background can transition to reveal the body
        "You crouch, pry the device from his grip."

        "The moment you press play, the audio crackles to life."
        "The cold seems to deepen around you."
        "You listen."

        # [BEGIN LOG]
        # Alpha‑4 (focused, analytical):
        a4 "…breaching through the roof. No lights inside. The whole interior's coated in frost. Human‑shaped figures everywhere… not debris. They look like statues."
        #Alpha‑8 (uneasy, sarcastic):
        a8 "Statues? Yeah, right. These things look way too damn real. Give me the chills."
        #Alpha‑10 (trying to stay calm):
        a10 "Keep spacing. Don't touch anything. The temperature's dropping fast."

        # Alpha‑4:
        a4 "…moving toward the generator. If we get power back, maybe we can see what we're dealing with. The air's getting colder the deeper we go. Doesn't feel natural."
        # Alpha‑8:
        a8 "Nothing about this place feels natural. It's like walking into a freezer that hates us."
        # Alpha‑10:
        a10 "Generator's ahead. Let's just get this done."

        #[STATIC — LIGHTS FLICKER ON]
        #Alpha‑10 (shouting):
        a10 "—movement above us!"
        #Alpha‑8:
        a8 "Those are NOT statues!"

        #Alpha‑4 (voice low):
        a4 "…something in the center of the warehouse. Large. Humanoid silhouette. It's emitting a cold field—everything around it is freezing instantly. It's just… standing there. Watching us."
        # Alpha‑8 (whispering):
        a8 "Why the hell is it just staring? Shouldn't it be attacking or something?"
        # Alpha‑10:
        a10 "Don't provoke it. Back away—slowly."

        #Alpha‑4:
        a4 "…frost spreading across the floor like it's alive. We need to fall back—now."
        #Alpha‑10:
        a10 "The door's jammed! Metal's brittle—trying to force it—"
        # [METAL STRAINING — CRACKING]
        # Alpha‑8:
        a8 "Come on, come on—damn it!"

        #Alpha‑4:
        a4 "…entity's advancing. Not fast. Like it's herding us. Why isn't it attacking?"
        #Alpha‑10 (panicking):
        a10 "Cold's climbing up my armor… can't feel my—"
        #[AUDIO WARBLE — SIGNAL DISTORTION]

        #Alpha‑4 (fading voice):
        a4 "…don't turn on the lights… that's what woke it… it was dormant…"
        #Alpha‑8 (voice shaking):
        a8 "We shouldn't have touched anything… damn it…"

        #Alpha‑10:
        a10 "…if anyone hears this… the outpost… center of the map…"
        #Alpha‑4:
        a4 "…it wasn't killing us… it was keeping us…"
        #[UNINTELLIGIBLE WHISPERING — MULTIPLE HUMAN‑LIKE LAYERS]
        "…here…" # Not sure whose voice this should be.
        #[END LOG]

        "After going through the log, you suddenly felt a shivering sensation behind you."
        "Turning around, you see it, what Alpha 4 was mentioning in the audio log."

        #Reveal Ice Boss
        "You raised your weapon."

        menu:
            "Stand Your Ground":
                jump fw_A
            "Circle and Evade":
                jump fw_B
            "Aggressive Push":
                jump fw_C
            "Retreat and Reposition":
                jump fw_D

    label fw_A:
        "You plant your feet. Rifle up. Breath steady."

        "It charges without hesitation."

        "You fire controlled bursts."

        "Each round bites into the ice plating, carving fractures across its body. Shards explode outward, clattering across frozen concrete. It doesn't slow—but it doesn't adapt either. It's committed to the straight line."

        "It swings."

        "You duck, the frozen blade smashing into a wall behind you and spiderwebbing steel."

        "You keep firing."

        "Closer."

        "Closer."
        
        "Then you see it—a faint pulse buried in the center of its chest, buried under layers of ice and flesh."

        "You don't rush. You wait for the rhythm."

        "The shot lands clean."

        "Then You decide to run away"
        jump fw_good_ending

    label fw_B:
        "You move instantly."

        "It strikes where you were a second ago, freezing the ground solid on impact."

        "You circle wide, forcing it to turn—slowly at first, then increasingly erratic as it loses traction in the shifting mist."

        "You fire between movement windows. Controlled, disciplined bursts.
        Cracks spread along its frame."

        "It accelerates—too fast now, overcommitting."

        "It lunges again."

        "You slide under its arc, pivot mid-motion, and fire into its exposed side."

        "The glow beneath the ice flickers."

        "It stumbles—just slightly."

        "That's all you need."

        "A final burst hits the weakened core."

        "The creature halts, rigid."

        "Then You decide to run away"
        jump fw_good_ending

    label fw_C:
        "You don't give it space."

        "You rush it."

        "It reacts instantly—wide swing—but you're already inside its reach.
        Your first shot hits at point-blank range, blasting ice off its torso. Frost climbs your arm interface, warning indicators flashing—but you override the pain feedback."

        "You drive forward."

        "Another shot. Then a strike with your weapon stock, cracking through reinforced ice layers."

        "The creature grabs for you—but its grip is unstable, fragmented.
        You twist free."

        "The chest glow is fully exposed now."

        "You press in."

        "One final shot at contact range."

        "The core collapses inward."

        "Then You decide to run away"
        jump fw_good_ending

    label fw_D:
        "You disengage immediately, falling back toward the dock edge."

        "The creature follows—but it hesitates now, as if learning your pattern too slowly to matter."

        "You use the environment: crates, steel pillars, container stacks. Every angle becomes cover, every gap a firing lane."

        "Each time it emerges from the mist, you punish it with precision shots.
        Not enough to finish it quickly—but enough to destabilize it.
        It grows more unstable, its movements stuttering."

        "Then it overextends—smashing through a crate to reach you."

        "That's the opening."

        "Fully exposed in the broken debris field."

        "You steady your rifle."

        "One clean sequence of fire."

        "The core collapses."

        "The creature freezes mid-motion—"

        "Then breaks apart into inert ice fragments across the loading dock floor."

        "Then You decide to run away"
        jump fw_good_ending

    label fw_good_ending:
        $ rifle_ammo = True
        "You run back to the police station to recoup yourself, along the way you find some rifle ammo."
        jump area_menu


    label fw_End:
        #This and fw_Death should be combined for the flavor text of fw_bad_ending
        "You turn and sprint for the gate."
        "Behind you, something moves—fast, wrong, closing the distance in bursts that don't match reality."
        "Your boots slam against frozen pavement, slipping for half a step before catching again."
        "Your HUD screams warnings—temperature collapse, signal distortion, unknown entity proximity—"
        "You don't look back. The fallen gate is just ahead. Then—"
        "A sound. Not a roar. Not a scream. A voice. Layered. Distorted. Familiar."

        a4 "—don't leave—"
        "Your stride falters."
        "You risk a glance over your shoulder."
        "Mist surges across the yard like a living tide. Inside it, shapes flicker—figures reaching, collapsing, reforming—Running with you."
        "No—{i}being dragged{/i}."

        "The temperature spikes downward again. Ice crawls up your legs, locking your joints mid-stride." #Maybe accompany with SFX
        "You stumble, crash hard onto the frozen concrete."
        "Your rifle skids away, disappearing into the mist."
        "The gate is only a few feet ahead."
        "You try to crawl. Your fingers don't respond."

        "The voice comes again, clearer now. Closer."
        a4 "—stay—"

        "A shadow falls over you. The mist pulls back just enough for you to see it standing there—taller than before, broader, its surface rippling with frozen silhouettes."
        "One of them turns toward you."
        "Alpha-4"

        "His arm lifts slowly, pointing—not at you—but past you."
        "Back toward the warehouse."
        "Your HUD flashes one final time." 
        "{b}SIGNAL ACQUIRED: ALPHA TEAM (ALL){/b}"
        "The cold consumes everything. Your vision fades to white."
        "The last thing you feel is movement—Not being attacked. Not being killed. But being pulled."
        "{b}Back inside{/b}"
        jump fw_death
    
    label fw_Fight:
        "You steady your aim."
        "The thing in the mist shifts—tall, jagged, its form breaking and reforming like ice cracking under pressure. 
        Frost spreads outward from its limbs, crawling across the ground in branching veins."

        #Ice Beast appears on screen
        "Your visor flickers."
        "{b}Temperature warning: critical.{/b}"
        "You open fire."

        "The shot echoes like a thunderclap in the frozen yard. The round strikes its torso—if it has one—but instead of blood, the impact blossoms into a burst of crystalline shards."
        "It doesn't slow. It {i}learns{/i}."

        "The creature lunges forward, movements unnatural, skipping frames like corrupted footage. One moment it stands at the loading dock—the next, it's halfway to you."
        "Your rifle chatters, each shot fracturing pieces off it, but those pieces don't fall. They hover." #I guess have gunshot audio in the background
        "Then snap back into place."

        "Your HUD glitches harder now—signals spiking, Alpha-team signatures merging, overlapping—Becoming one." #I want to say this could be shown visually, but I doubt Jordan has time for that.
        "The creature shrieks—a sound like metal screaming under stress—and the temperature plummets again."

        "Your joints stiffen. Your breath stops fogging. You realize—"
        "It's not getting colder. You're freezing."
        "The creature reaches you."
        "For a split second, you see through the ice forming across its surface—faces."
        
        #Reveal fused faces
        "Alpha-4"
        "Alpha-8"
        "Alpha-10"
        #"All fused beneath the frozen shell, eyes open, mouths moving silently."
        "Your weapon locks up. So do your hands."
        "The last thing your visor records is the entity leaning closer, its surface cracking open—"
        "{b}Inviting you in.{/b}"
        jump fw_death


    label fw_death:
        "{b}You Died{/b}"

        "Return to start of area?"
        menu:
            "yes":
                jump frozen_warehouse
            "no":
                $ used_areas["frozen_warehouse"] = False
                jump area_menu                


    # ─────────────────────────────────────────
    #  FLESH WALKER End
        # this text should be moved from this unused label into one of the currently used on (during the rounds of alien town)    
    # ─────────────────────────────────────────
    label aleintown_End:
        # this text should be moved from this unused label into one of the currently used on (during the rounds of alien town)        
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
        # this text should be moved from this unused label into one of the currently used on (during the rounds of alien town)
        jump at_bad_ending

    # ─────────────────────────────────────────
    #  FLESH WALKER MINIGAME — minigame.rpy
    # ─────────────────────────────────────────
    # label flesh_Walker_Boss:
    #     call flesh_walker_minigame
    #     if fw_health > 0:
    #         "You made it through."
    #     else:
    #         jump death
    
    # ─────────────────────────────────────────
    #  Mutated Forest
    # ─────────────────────────────────────────
    label mutated_forest:
        "flavor all the text"

        "Stalker at tower, kill or run"

        "gain star or death?"

        menu:
            "star":
                jump mf_star
            "death":
                jump mf_death

    label mf_star:
        $ star_count += 1        
        jump area_menu

    label mf_death:
        "{b}You Died{/b}"

        "Return to start of area?"
        menu:
            "yes":
                jump mutated_forest
            "no":
                $ used_areas["mutated_forest"] = False
                jump area_menu  

    # ─────────────────────────────────────────
    #  Last City Ruins
    # ─────────────────────────────────────────
    label city_ruins:

    # ─────────────────────────────────────────
    #  Alien Amusement-Park
    # ─────────────────────────────────────────
    label alien_amusement_park:

    # ─────────────────────────────────────────
    #  Secret Area
    # ─────────────────────────────────────────
    label secret_outpost:
    
    # This ends the game.
    return

    label end_of_demo:
        "{b}THANK YOU FOR PLAYING{/b}"