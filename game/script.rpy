# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the name of the character.

define mc = Character(_("Me"), color="#12da00")
define a7 = Character(_("Alpha-7"), color="#3f99ff")
define a4 = Character(_("Alpha-4"), color="#263cff")
define a8 = Character(_("Alpha-8"), color="#263cff")
define a10 = Character(_("Alpha-10"), color="#263cff")
define a11 = Character(_("Alpha-11"), color="#263cff")
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
image bg FrozenWarehouse = im.Scale("bg FrozenWarehouse.png", 1920, 1080)
# All background images going forward should be in 1920x1080 resolution.

image Tablet = im.Scale("bg Tablet-2.png", 1920, 1080)
image Fleshwalker = im.Scale("Fleshwalker-2.png", 1920, 1080)
image Ice-Wolf = im.Scale("icewolf.png", 1920, 1080)
image Sand-Worm = im.Scale("sandworm.png", 1920, 1080)

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

    "You wake up with a sharp ache across your lower torso. The cold floor presses against your cheek, and your vision swims as you try to remember where you are—or what happened."

    "The room around you is dim, lit by a few flickering ceiling lights. As your eyes adjust, you make out a dilapitated sign on the far wall:"

    "{b}CHARLESWOOD POLICE DEPARTMENT{/b}"

    "You push yourself upright. Your uniform is torn, but the insignia on your shoulder—{b}Recon Unit{/b}—is still visible."

    "You remember the mission. You remember the boss. You remember pain. 
    Everything after that is blank."

    "Across the room you spot something—another body."

    "A recon uniform, same as yours, slumped against a wall, unmoving. You kneel beside them, checking for anything useful." 
    "Their equipment belt holds a {b}rifle{/b} with an empty chamber and a {b}sidearm{/b} with a single full magazine. You take both. Training, not instinct."

    "As you search further, you find something tucked beneath their arm:
    A {b}tablet{/b}, still powered on."

    "As you take a closer look, you see multiple dots flickering on a map."

    # Transition to the tablet screen
    # Add audio effects
    
    # If there is a transition that leads to the pop up to explore other areas that'd be great.
    # Couldn't find anything like that so I don't know if it even exists.

    "Choose an area to explore:"
    jump area_menu

        "The Last City Ruins" :
            jump the_Last_City_Ruins

        "Alien Amusement Park" :
            jump alien_Amusement_Park
    label area_menu:
        # prob should have it's own background (or something)
        scene bg AlienTown
        show Fleshwalker at right 
        scene bg PoliceDepartment
        show Tablet at center
        # with fade
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
            "{b}End of Demo{/b}" if (used_areas["frozen_warehouse"] and used_areas["alien_town"]):
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
            # "Explore Secret Outpost" if not used_areas["secret_outpost"]:
            #     "You feel unprepared. Continue anyways?"
            #     menu:
            #         "Yes":
            #             "Are you really sure?"
            #             menu:
            #                 "Yes":
            #                     $ used_areas["secret_outpost"] = True
            #                     jump secret_outpost
            #                 "No":
            #                     jump area_menu
            #         "No":
            #             jump area_menu

        return

    # ─────────────────────────────────────────
    #  Alien Town
    # ─────────────────────────────────────────
    label alien_town:
        #Scene changes to the outskirts of the Alien Town.
        scene bg AlienTown
        with fade 

        "The tablet's signal leads you to the outskirts of a small settlement.
        From a distance, the houses look almost cheerful, painted in bright colors."

        "But the closer you get, the more wrong everything feels.
        Your tracker vibrates once."

        "{b}ALPHA-TEAM SIGNALS DETECTED — MULTIPLE SOURCES{/b}"

        "{b}All{/b} of them are somewhere inside the cornfield ahead."

        # Change scene to cornfield
        # Not sure if there is supposed to be ambient sounds of birds and insects. Describing the sounds seems weird
        "The corn towers over you—far taller than it should be.
        The stalks are a soft, rubbery texture. Not like plants. More like skin."

        "Your tracker pings again."
        "{b}ALPHA-5 — LAST POSITION: 42m{/b}"
        "You keep moving."

        # Tightening cornfield path. Really feels like this should be a new scene but idk.
        "The deeper you go, the narrower the path becomes.
        You push the corn aside and the stalks bend like muscle, not plant fiber."

        # Scene changes and reveals a house
        # "Up close, the walls pulse faintly, like they're breathing." -Not sure how pulsing walls are gonna look
        "Your tracker vibrates."
        "{b}ALPHA-5 — LAST POSITION: 3m{/b}"

        mc "This is the place."
        # Scene changes to the inside of the house I guess?
        "You step inside."

        #Scene change again:
        "The room is empty—except for a single boot lying in the center of the floor. The floor beneath it bulges upward in a human-shaped outline, frozen mid-struggle."
        #"The walls around the outline are stretched, as if something inside them pushed outward before being pulled back in."
        #"A sidearm lies nearby, bent at an impossible angle."
        #The above 2 lines feel weird to narrate. IDK if it'll be possible to explain this just visually. Or if Jordan will have time.
        mc "This is where Alpha-7 died."

        "Next to it, half-melted into the fleshy floor, is a small recording device. It crackles to life, as you pry it free."
        
        #[BEGIN LOG]
        a7 "…Alpha-7 …we touched down near the town at dusk. Looked abandoned from a distance. Alpha‑3 ordered recon. Standard sweep. We split up to check the structures. Empty rooms, empty streets…"
        a7 "…first contact hit after nightfall. Fast. Sharp. Rounds didn't slow it. It didn't even try to kill us—just herded us deeper into the town."
        #[AUDIO DISTORTION — ORGANIC SHIFTING]
        a7 "…that's when I saw it. Flesh‑colored. Limbs like stretched muscle."
        a7 "…it tore through the others. I ran. The houses shift when you're not looking. I swear I can hear them whispering under the floorboards."
        a7 "…I'm inside now. Walls feel closer. I think it knows I'm here."
        #[WEAPON CHAMBERING]
        a7 "…if anyone finds this… don't stay here. Don't touch the walls. Just keep moving and get the hell out…"
        # [STATIC — SIGNAL COLLAPSE]
        "{b}End of Log{/b}"

        "Looking out the window, you notice that dusk approaches. As you turn to leave, the house shifts behind you."

        jump round_1

        
    label round_1:
        scene bg AlienTown
        show Fleshwalker at right 
        call action_menu from _call_action_menu
        jump round_2

    label round_2:
        call action_menu from _call_action_menu_1
        jump round_3

    label round_3:
        call action_menu from _call_action_menu_2
        jump at_end_game

    # -------------------------
    # ACTION MENU (DYNAMIC)
    # -------------------------

    label action_menu:

        menu:

            "Look for cover in the house" if not (used_cover or used_grenade):
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
        "You use your rifle and fire at the enemy, dealing great damage to it."
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
        "You succesfully shoot the enemy, it deals moderate damage, but it's still up and coming toward you."
        return

    label sidearm_fail:
        $ boss_points -= 1
        "The gun us empty, you jump back in the nick of time but it's nails scratch you."
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
        "You spend too much time looking for it and get clobbered to the floor, you get up and look for other options."
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
        "You succesfully get away from the enemy, and go back to the police hub to recouperate."
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
            "Yes":
                jump alien_town
            "No":
                $ used_areas["alien_town"] = False
                jump area_menu

            
    
    # ─────────────────────────────────────────
    #  Frozen Ghost Warehouse
    # ─────────────────────────────────────────
    label frozen_Ghost_Warehouse:
        #Scene change to I think a town? We'll later change to the warehouse itself, but before that, not sure what it's supposed to be.
        scene bg FrozenWarehouse
        with fade 

        "Your tablet lights up with multiple overlapping pings—{b}3 Alpha-team signatures{/b} clustered in the same location."
        "The signals are faint, flickering, as if something is interfering with them."
    label frozen_warehouse:
        scene grey

        #Scene change to I think a town? We'll later change to the warehouse itself, but before that, not sure what it's supposed to be.
        "Your tablet lights up with multiple overlapping pings—clustered in the same location."

        "You follow the alleyway until it opens into a wide loading district. 
        A massive warehouse dominates the block, its metal walls coated in a thick layer of frost."

        mc "It looks like a blizzard hit this one building and nowhere else."

        #Scene changes to reveal the warehouse
        "The warehouse is secured with a heavy chain, yet the metal has turned so brittle from cold that it snaps the moment you strike at it."

        "As you step inside the warehouse, you notice something wrong near the loading dock."
        "The door is jammed halfway, frost clings to the edges of the metal, forming jagged crystalline teeth. And a body lays wedged in the gap beneath the door—cut cleanly in half."
        "You approach slowly, the insignia on the shoulder is unmistakable: {b}ALPHA-4{/b}. His outstretched hand is frozen to the concrete, fingers curled around a small recording device." 

        "The moment you press play, the audio crackles to life."

        # [BEGIN LOG]
        # Alpha‑4 (focused, analytical):
        a4 "…breaching through the roof. No lights inside. The whole interior's coated in frost."
        a10 "Keep spacing. Don't touch anything. The temperature's dropping fast."

        # Alpha‑4:
        a4 "…moving toward the generator. If we get power back, maybe we can see what we're dealing with."
        a10 "{b}Hold!{/b} Alpha-8, investigate that humanoid object at 2 o'clock."

        #Alpha‑4 (voice low):
        a4 "…something in the center of the warehouse. Large. It's emitting a cold field—everything around it is freezing instantly. It's just… standing there. Watching us."
        # Alpha‑8 (whispering):
        a8 "Why the hell is it just staring? Shouldn't it be attacking or something?"
        # Alpha‑10:
        a10 "Don't provoke it. Back away—slowly."

        a8 "The door's jammed! Metal's brittle, I'm going to force it—"
        # [METAL STRAINING — CRACKING]
        # Alpha‑8:
        a10 "Are comms working?! Alpha-4, request support!"

        #Alpha‑4:
        a4 "…The entity's advancing. Not fast. More like it's sheparding us. Why isn't it attacking?"
        #Alpha‑10 (panicking):
        a8 "Cold's climbing up my armor… can't feel my—"
        #[AUDIO WARBLE — SIGNAL DISTORTION]
        "{b}BANG!{/b}"
        "{b}End of Log{/b}"
        #[END LOG]

        "The log ends with a loud noise, and you feel a shivering sensation behind you."
        "Turning around, you see it, what was mentioned in the audio log, awoken by the sound."

        #Reveal Ice Boss
        "You raise your weapon."
        jump fw_menu

    label fw_menu:
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
        "You plant your feet. Rifle up. Breath steady. 
        It charges without hesitation."

        "You fire controlled bursts."

        "Each round bites into the ice plating, carving fractures across its body. Shards explode outward, clattering across frozen concrete. It doesn't slow—but it doesn't adapt either. It's committed to the straight line."

        "You duck a swing, the frozen blade smashing into a wall behind you and spiderwebbing steel."

        "You keep firing. Closer"

        "And even closer."

        "Then you see it—a faint pulse buried in the center of its chest, buried under layers of ice and flesh."

        "You don't rush. You wait for the rhythm."

        "The shot lands clean, stunning the entity."

        "Then, you decide to run away."
        jump fw_good_ending

    label fw_B:
        "You move instantly."

        "It strikes where you were a second ago, freezing the ground solid on impact."

        "You circle wide, forcing it to turn—slowly at first, then increasingly erratic as it loses traction in the shifting mist."

        "You fire between movement windows. Controlled, disciplined bursts.
        Cracks spread along its frame."

        "It accelerates—too fast now, overcommitting."

        "You slide under its arc, pivot mid-motion, and fire into its exposed side."

        "The glow beneath the ice flickers. It stumbles—just slightly. That's all you need."

        "A final burst hits the weakened core. The creature halts, rigid."

        "Then, you decide to run away."
        jump fw_good_ending

    label fw_C:
        "You don't give it space. You rush it instantly."

        "It reacts simultaneously—a wide swing—but you're already inside its reach."

        "Your first shot hits at point-blank range, blasting ice off its torso. Frost climbs your arm, warning indicators flashing—but you drive forward."
        
        "Another shot. Then a strike with your weapon stock, cracking through reinforced ice layers."

        "The creature grabs for you—and catches true. You try to slip out, but are unable to with both your arms frozen solid."

        "The creatures chest glow is fully exposed now. But so is your head."

        "One final shot at contact range would do it in, but before you can, it goes for the kill."

        jump fw_bad_ending

    label fw_D:
        "You disengage immediately, falling back toward the dock edge."

        "The creature follows—with unexpected restrain."

        "You use the environment: crates, steel pillars, container stacks. Every angle becomes cover, every gap a firing lane."

        "Each time it emerges from the mist, you punish it with precision shots.
        Not enough to finish it quickly—but enough to destabilize it."

        "Then it overextends—smashing through a crate to reach you."

        "That's the opening. Fully exposed in the broken debris field. You steady your rifle. One clean sequence of fire."

        "The core collapses. The creature freezes mid-motion—Then breaks into fragments scattered across the ground. Covering the floor like crystals."

        "Then, you decide to run away."
        jump fw_good_ending

    label fw_good_ending:
        $ rifle_ammo = True
        $ star_count += 1
        "You run back to the police station to recoup yourself, along the way you find some rifle ammo."
        jump area_menu

    label fw_bad_ending:
        "Try again?"
        menu:
            "Yes":
                jump fw_menu
            "No":
                $ used_areas["frozen_warehouse"] = False
                jump area_menu


    # label fw_End:
    #     #This and fw_Death should be combined for the flavor text of fw_bad_ending
    #     "You turn and sprint for the gate."
    #     "Behind you, something moves—fast, wrong, closing the distance in bursts that don't match reality."
    #     "Your boots slam against frozen pavement, slipping for half a step before catching again."
    #     "Your HUD screams warnings—temperature collapse, signal distortion, unknown entity proximity—"
    #     "You don't look back. The fallen gate is just ahead. Then—"
    #     "A sound. Not a roar. Not a scream. A voice. Layered. Distorted. Familiar."

    #     a4 "—don't leave—"
    #     "Your stride falters."
    #     "You risk a glance over your shoulder."
    #     "Mist surges across the yard like a living tide. Inside it, shapes flicker—figures reaching, collapsing, reforming—Running with you."
    #     "No—{i}being dragged{/i}."

    #     "The temperature spikes downward again. Ice crawls up your legs, locking your joints mid-stride." #Maybe accompany with SFX
    #     "You stumble, crash hard onto the frozen concrete."
    #     "Your rifle skids away, disappearing into the mist."
    #     "The gate is only a few feet ahead."
    #     "You try to crawl. Your fingers don't respond."

    #     "The voice comes again, clearer now. Closer."
    #     a4 "—stay—"

    #     "A shadow falls over you. The mist pulls back just enough for you to see it standing there—taller than before, broader, its surface rippling with frozen silhouettes."
    #     "One of them turns toward you."
    #     "Alpha-4"

    #     "His arm lifts slowly, pointing—not at you—but past you."
    #     "Back toward the warehouse."
    #     "Your HUD flashes one final time." 
    #     "{b}SIGNAL ACQUIRED: ALPHA TEAM (ALL){/b}"
    #     "The cold consumes everything. Your vision fades to white."
    #     "The last thing you feel is movement—Not being attacked. Not being killed. But being pulled."
    #     "{b}Back inside{/b}"
    #     jump fw_death
    
    # label fw_Fight:
    #     "You steady your aim."
    #     "The thing in the mist shifts—tall, jagged, its form breaking and reforming like ice cracking under pressure. 
    #     Frost spreads outward from its limbs, crawling across the ground in branching veins."

    #     #Ice Beast appears on screen
    #     "Your visor flickers."
    #     "{b}Temperature warning: critical.{/b}"
    #     "You open fire."

    #     "The shot echoes like a thunderclap in the frozen yard. The round strikes its torso—if it has one—but instead of blood, the impact blossoms into a burst of crystalline shards."
    #     "It doesn't slow. It {i}learns{/i}."

    #     "The creature lunges forward, movements unnatural, skipping frames like corrupted footage. One moment it stands at the loading dock—the next, it's halfway to you."
    #     "Your rifle chatters, each shot fracturing pieces off it, but those pieces don't fall. They hover." #I guess have gunshot audio in the background
    #     "Then snap back into place."

    #     "Your HUD glitches harder now—signals spiking, Alpha-team signatures merging, overlapping—Becoming one." #I want to say this could be shown visually, but I doubt Jordan has time for that.
    #     "The creature shrieks—a sound like metal screaming under stress—and the temperature plummets again."

    #     "Your joints stiffen. Your breath stops fogging. You realize—"
    #     "It's not getting colder. You're freezing."
    #     "The creature reaches you."
    #     "For a split second, you see through the ice forming across its surface—faces."
        
    #     #Reveal fused faces
    #     "Alpha-4"
    #     "Alpha-8"
    #     "Alpha-10"
    #     #"All fused beneath the frozen shell, eyes open, mouths moving silently."
    #     "Your weapon locks up. So do your hands."
    #     "The last thing your visor records is the entity leaning closer, its surface cracking open—"
    #     "{b}Inviting you in.{/b}"
    #     jump fw_death


    # label fw_death:
    #     "{b}You Died{/b}"

    #     "Return to start of area?"
    #     menu:
    #         "yes":
    #             jump frozen_warehouse
    #         "no":
    #             $ used_areas["frozen_warehouse"] = False
    #             jump area_menu                


    # # ─────────────────────────────────────────
    # #  FLESH WALKER End
    #     # this text should be moved from this unused label into one of the currently used on (during the rounds of alien town)    
    # # ─────────────────────────────────────────
    # label aleintown_End:
    #     # this text should be moved from this unused label into one of the currently used on (during the rounds of alien town)        
    #     #Scene changes to night time cornfield
    #     "You can hear the creature catching up to you at a rapid speed."
    #     "You pull out your pistol and put a couple of rounds down into the cornfield behind you to no avail."
    #     "Continue sprinting, you can feel the exhaustion. You are running out of breath. With no bearings where you are. You slow down and start to listen."
    #     # Only breath sounds

    #     "Has the monster moved on? No. It's here."
    #     #Footstep audio
    #     "You suddenly hear footsteps from {b}behind{/b}."
    #     "You turn and fire your rifle, emptying the magazine." #Insert 30 seconds of nonstop full auto until a click sound.

    #     mc "Shit!"
    #     "You're out of ammo."

    #     "You here it next to you, breathing down your neck and before you can react you can only hear the crunch of your ribs."

    #     "You escape into a house and barricade all the doors."
    #     "You turn a table over and point your rifle at the only entrance to the house."
    #     "You can hear it rounding the house, as if cornering its prey." #Not sure how the audio is going to go
    #     "You grip the rifle tight in your hand trying to not recall what had happened to Alpha 7."
    #     "Then the rounding sound stopped, and the only sound you can hear is the sound of your own breath." #Play appropriate audio
    #     fw "...I'm inside now. Walls feel closer. Something's moving under the floor. I think it knows I'm here."
    #     "Before you can react, a pair of sharp claws impales your chest and dragged you though the window."
    #     "You swore was a wall when you barricaded yourself in."
    #     # this text should be moved from this unused label into one of the currently used on (during the rounds of alien town)
    #     jump at_bad_ending

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
    label the_Last_City_Ruins:
        "The city ruins stretch out before you like a sun‑bleached graveyard."
        "Heat ripples across the cracked asphalt. Sand drifts in slow waves between collapsed skyscrapers. The air tastes metallic, dry, and dead."
        "Your visor pings."
        "A {b}red marker{/b} blinks on your HUD — Alpha‑12’s last known location."
        "But something is wrong. The marker is {b}moving{/b}."
        "Slowly. Steadily. Directly toward you."
        "You frown behind your visor."
        "Alpha‑12 shouldn’t be moving. Not like this. Not this fast."
        "The marker accelerates. You take a step back. The ground vibrates beneath your boots."
        "A low, resonant rumble rolls through the ruins — deep enough to shake dust from the broken windows above."
        "Your HUD flickers. The marker surges forward."
        "Too fast. Far too fast to be human."
        "A cold realization hits you."

        mc "... That’s not Alpha‑12."
        "The sand ahead bulges upward. Cracks spiderweb across the street. Metal groans beneath shifting earth."
        "The rumble grows louder. Closer"
        "The red marker blinks violently — then disappears."
        "The ground {b}erupts.{/b}"
        "A massive Sandworm bursts through the street in an explosion of sand, concrete, and shattered rebar."
        "Its armored hide glistens in the sun. Its maw opens wide, lined with spiraling rings of teeth."
        "The shockwave knocks you backward."
        "You scramble to your feet as the worm slams back into the ground, tunneling beneath the ruins."
        "The street collapses behind you as you sprint."

        "Every few seconds, the earth bulges — a warning before the creature bursts upward again, jaws snapping shut where you stood moments before."
        "Heat. Dust. Screams of twisting metal."
        "The city becomes a collapsing maze."
        "You dive behind a toppled bus as the worm erupts again, sand pouring through shattered windows like a waterfall."

        "You're breathing hard. Your legs burn. Your visor is fogged with sweat."
        "The worm circles back. The ground trembles violently. You brace yourself—"
        "A hand grabs your shoulder from behind."
        "Before you can react, someone yanks you backward, dragging you through a narrow hatch in the side of an abandoned tank."

        #Scene should be whatever tank interior we're in.
        "{i}The hatch slams shut above you. Sand pours down the sides of the tank like a collapsing dune.{/i}"
        "{i}Alpha‑11 drops in after you, breathing hard, dust streaking his cracked visor. He braces himself against the wall, listening to the rumbling outside.{/i}"
        
        #Sprite of Alpha-11 would be here normally
        a11 "…You okay? That thing nearly swallowed you whole. I had to shove you in here before it surfaced again."
        a11 "…Yeah. That’s a Sandworm. A big one in fact, It’s been circling this district since I got here."
        a11 "…You were tracking Alpha‑12, right? Did you see him? Did you find him?"
        a11 "…I lost him when the ground gave out. One second he was right behind me, the next… the sand swallowed half the street."
        a11 "…I tried to reach him. I swear I did. But the worm was already circling back. I had to run."
        a11 "…Please. Tell me you saw him. Anything. A signal. A trail. Did he make it out?"
        a11 "…What about the others? Alpha‑4? Alpha‑8? Alpha‑10? Anyone from the other teams?"
        a11 "…Are any of them still alive?"

        menu:
            "No":
                jump cont_Last_City_Ruins
            "I don't know":
                jump cont_Last_City_Ruins

    label cont_Last_City_Ruins:
        "The silence that follows is heavy. Alpha 11 exhales, steadying himself."
        a11 "Alpha‑12 found me after I escaped the forest."
        a11 "He kept me moving. Got me through the heat, the sand, the ruins. I owe him for that."
        a11 "But this city… It's a graveyard. Collapsed towers, cracked streets, skeletons everywhere. And under all that? That monster."
        a11 "Alpha‑12 pushed me out of the way when the ground buckled. Told me to run. I thought he was right behind me."
        a11 "But when I turned around...he was gone."

        a11 "So tell me again. You didn’t see him? No sign at all?"
        a11 "I need to know if he’s still out there."
        "The tank shakes as the Sandworm tunnels deeper beneath the ruins. Alpha‑11 grips the hatch wheel."
        a11 "When that thing moves on, we’re heading east. That’s where the exit should be. If Alpha‑12 made it out, that’s where he’d go."
        a11 "We’ll keep looking. Until we know for sure."
        a11 "Get ready. We move as soon as it’s clear."

        "The rumbling outside fades into the distance. Only then does Alpha‑11 release his grip on the hatch wheel."
        a11 "Alright. It’s moving on. You go first."
        #Scene changes back to what it originally was
        "You climb out of the tank and scan the ruins — sun‑bleached streets, leaning skyscrapers, dunes swallowing entire vehicles."
        "Your visor pings softly."
        "{b}Alpha‑12’s tracker signal is still active.{/b}" 
        "Still moving. Still attached to the Sandworm’s body."
        "Alpha‑12 is gone. The worm is wearing his beacon like a trophy."
        "You swallow hard. Alpha‑11 doesn’t know."

        mc "Clear!"
        "Alpha‑11 tries to climb out on his own."
        "He gets one foot onto the ladder — and immediately winces, doubling over as pain rips through his abdomen."
        "He grips the rung with one hand, the other pressed against his stomach."
        a11 "I’ll go first."
        a11 "I can make it to the pharmacy. I’ll find Alpha‑12 on the way."
        "He tries again. His leg buckles."
        "He slips."

        "You grab his arm before he falls back into the tank"
        mc "Stop. You're hurt."
        a11 "I have to go"
        a11 "If Alpha‑12 is out there, he’ll head for the pharmacy. I need to—"

        "Alpha-11 tries to pull away from you, but his strength fails."
        "He collapses onto the tank’s hull, one hand clamped over his wound."
        mc "Let me see."
        "The bandage is soaked through. The wound beneath is swollen, darkened, pulsing faintly with infection."
        a11 "It’s spreading faster than I thought."
        a11 "Which way? Where’s the pharmacy from here?"
        "Alpha-11 looks out over the ruins, voice quieter now."
        a11 "Tell me the direction. I’ll go. Just point me there."

        "He doesn’t know the truth."
        "That Alpha-12 is already dead."
        "That his tracker is on the Sandworm."
    # ─────────────────────────────────────────
    #  Alien Amusement-Park
    # ─────────────────────────────────────────
    label alien_amusement_park:
        "As you walk down the urban area, the last location of Alpha 9’s tracker flickers on your tablet. "
        "Suddenly, the weather changed dramatically; it seemed a hurricane was crashing down upon this side of the city. Every step you take forward feels more difficult than the last, until you eventually lose balance and are picked up into the air. "
        "Within the hurricane, you struggle to keep your balance while trying to make sure nothing is lost, until you see a light centered in the eye of the hurricane."
        "It is taking you closer and closer as if the wind is forcefully taking you into the center. You turned and immediately grabbed onto something."
        "However, something suddenly breaks, and you are launched into the eye of the hurricane."

        "As you wake up with a gasp, you study the surroundings around you, and what was in front surprised you to the core."
        mc "Is that an...amusement park?"

        "You stand up, pad yourself down, and slowly walked closer to the entrance. "
        "Warning: operator field symbols detected."

        "Warning: operator field symbols detected."
        show Tablet

        "Within an emergency situation, recon members may leave specific field symbols for other members in case they will be entering a large area without an audio record or if the record is ineffective."
        "Operatives are to be extremely careful in the event that they do encounter these symbols, as the circumstances of their usage often mean a deadly environment."
        "You looked around the entrance and found a field symbol."

        "Knowing the risk, you first surveyed the area around the entrance to no use; the wall of the entrance gate stretched across infinite distances. As in fact someone or something is giving you an undefiable urge to immediately enter the park"
        "Without hesitation, you quickly opened the gate and entered the park."

        "After entering the park, you noted there really isn't a park, but one specific building in front of you"
        "Walking around the building proved to be useless, as somehow you always manage to route back to the entrance of that building."
        "Guess there is no other choice. You entered the building."
        "After entering the building, there are 4 doors present in front of you."
        "Then, suddenly, a black shadow figure appeared from your body. The shadow slowly walked towards the {b}first{/b} door and made a gesture, opening the door and facing through the door."

        menu:
            "Door 1"
            "Door 2"
            "Door 3"
            "Door 4"
    # ─────────────────────────────────────────
    #  Secret Area
    # ─────────────────────────────────────────
    
    label secret_outpost:
        if star_count == 0:
            jump so_0
        if star_count == 1:
            jump so_1
        if star_count == 2:
            jump so_2
        if star_count == 3:
            jump so_3
        if star_count == 4:
            jump so_4
        if star_count == 5:
            jump so_5
        if star_count == 6:
            jump so_6

    label so_0:
        "You get lost and die"

        "Restart?"
        menu:
            "Yes":
                $ used_areas["secret_outpost"] = False
                jump area_menu
            "No":
                jump end_of_demo
        return
    label so_1:
        # Replace "" with character images instead
        'You made a quick gasp and had woken upped within what seemed like a status pod. Suddenly a robotic arm hovered into your vision. It went up and pulled down a monitor.' 

        '“How are you today young man.”'

        'The monitor flashed opened. A figure suddenly appeared on the monitor screen. Your eyes flinched and you quickly covered it with your hand.' 

        '“I….Where is this?” '

        '“First, tell me about what you know young man.”' 

        menu:
            "Tell the truth":
                "I have been to this location and then I followed the orders and headed for the outpost."        
            "Lie":
                "I don't remember"

        '“Interesting…”'

        'You hears a familiar voice.'

        '“It seemes subject is not a candidate for replacement. Proceed with the amnestics .”' 

        '“Wait…what?”' 

        'Before you can react the status pod instantly closed, you tried to pry open the pod to no prevail. You can then smell gas slowly filling the pod. Before slowly falling asleep.'

        '10 minutes later. The pod opened again, and multiple flashlight flashed into the pod.' 

        '“Private wake up!” A voice came from outside the pod.'

        'You slowly opened your eyes. You tried to remember what had happened before but was there something happened before?' 

        '“Private, you have been though the simulation and your rank as officially been chosen.” The voice from outside continued.' 

        'You checked yourself then looked at the direction where the voice came from. It was a high ranked officer standing outside with a bunch of clothing on his hand.'

        'You slowly stepped out of the pod.' 

        '“Seemes like his memories are still fragmented. But its ok.”' 

        'Another figure dressed in a lab coat is whispering into the ear of the officer however you managed to catch their small talk.' 

        '“Private REDACTED though your honnorable service within the simulation command has granted you the rank of Sargent.”'

        'The officer shoved the clothing along with the metals towards and you accept the clothing. Then the officer salutes you, and out of instinct you saluted back.' 

        '“Sargent REDACTED The next assault will take place in 24:00 EST arrive with your assult squad at drop site at 23:00 EST for briefing.”'

        'The officer saluted again before turning and leaving. You started to dress.' 

        '“Good luck sargent, don’t keep Alpha team waiting.”'

        'The figure in lab coat smiled and left the room.' 

        'He sounded familiar but you can’t remember who.' 
        return
    label so_2:
        return
    label so_3:
        return
    label so_4:
        return
    label so_5:
        return
    label so_6:
        return
    
    # This ends the game.
    return

    label end_of_demo:
        "{b}THANK YOU FOR PLAYING{/b}"



#     # ─────────────────────────────────────────
#     #  Start Copy of Originial
#     # ─────────────────────────────────────────
# label start:

#     # Show a background. This uses a placeholder by default, but you can
#     # add a file (named either "bg room.png" or "bg room.jpg") to the
#     # images directory to show it.

#     # Start by playing some music.
#     # play music "audio/On-Lyne  PARTY OF YOUR LIFETIME Instrumental  Technocyte Coda Menu Theme - OliveOil (youtube).mp3"
#     scene bg PoliceDepartment
#     with fade

#     # This shows a character sprite. A placeholder is used, but you can
#     # replace it by adding a file named "eileen happy.png" to the images
#     # directory.
#     #show me

#     "You wake up with a sharp, pulsing ache across your lower torso. For a moment, you can't breathe. The cold floor presses against your cheek, and your vision swims as you try to remember where you are—or what happened."

#     "When you manage to roll onto your back, you see the bandages first. A long, horizontal wrap stretches across your lower abdomen, tight and clean. Someone treated the wound. 
#         Someone kept you alive. But you don't remember who."

#     "The room around you is dim, lit by a few flickering ceiling lights. Dust drifts lazily through the air. As your eyes adjust, you make out the cracked remains of a sign on the far wall:"

#     mc "{b}CHARLESWOOD POLICE DEPARTMENT{/b}"

#     "Most of the letters are missing or warped, but the meaning is clear enough. This was once a lobby. Now it feels abandoned—quiet in a way that doesn't feel natural."

#     "You push yourself upright, unsteady. Your uniform is torn, scorched in places. The insignia on your shoulder—{b}Recon Unit{/b}—is still visible, though faded. 
#         You remember the mission. You remember the boss. You remember pain."
    
#     "Everything after that is blank."

#     "You stagger forward, scanning the room. A collapsed desk. Scattered papers. A toppled chair. And then—another body."

#     "A recon uniform, same as yours. Same insignia & gear. They're slumped against a wall, unmoving. You kneel beside them, checking for anything useful." 
#     "Their equipment belt holds a {b}rifle{/b} with an empty chamber and a {b}sidearm{/b} with a single full magazine. You take both. Training, not instinct."

#     "As you search further, you find something tucked beneath their arm:"
#     "A {b}tablet{/b}, cracked but still functional."

#     "When you power it on, the screen flickers to life. A simple interface appears—clean, minimal, unmistakably military. One option is highlighted."

#     # Transition to the tablet screen
#     # Add audio effects
    
#     # If there is a transition that leads to the pop up to explore other areas that'd be great.
#     # Couldn't find anything like that so I don't know if it even exists.

#     "Choose an area to explore:"
#     jump area_menu

#     label area_menu:
#         # prob should have it's own background (or something)
#         scene bg AlienTown
#         show Fleshwalker at right 
#         scene bg PoliceDepartment
#         show Tablet at center
#         # with fade
#         menu:
#             # Does not open up others
#             "Explore Alien Town" if not used_areas["alien_town"]:
#                 $ used_areas["alien_town"] = True
#                 jump alien_town  

#             # Opens up ruins
#             "Explore Frozen Warehouse" if not used_areas["frozen_warehouse"]:
#                 $ used_areas["frozen_warehouse"] = True
#                 jump frozen_warehouse

#             # Only used for demo
#             "{b}End of Demo{/b}" if (used_areas["frozen_warehouse"] and used_areas["alien_town"]):
#                 jump end_of_demo

#             # # Opens up ruins
#             # "Explore Mutated Forest (wip)" if not used_areas["mutated_forest"]:
#             #     $ used_areas["mutated_forest"] = True
#             #     jump mutated_forest          

#             # # Opens up amusement park
#             # "{color=#0000ffff}Explore City Ruins (wip){/color}" if (not used_areas["city_ruins"] and (used_areas["mutated_forest"] or used_areas["frozen_warehouse"])):
#             #     $ used_areas["city_ruins"] = True
#             #     jump city_ruins

#             # # Does not open up others   
#             # "Explore Alien Amusement Park (wip)" if (not used_areas["alien_amusement_park"] and used_areas["city_ruins"]):
#             #     $ used_areas["alien_amusement_park"] = True
#             #     jump alien_amusement_park

#             # # Open from start, leads to different outcomes
#             # "Explore Secret Outpost" if not used_areas["secret_outpost"]:
#             #     "You feel unprepared. Continue anyways?"
#             #     menu:
#             #         "Yes":
#             #             "Are you really sure?"
#             #             menu:
#             #                 "Yes":
#             #                     $ used_areas["secret_outpost"] = True
#             #                     jump secret_outpost
#             #                 "No":
#             #                     jump area_menu
#             #         "No":
#             #             jump area_menu

#         return        

#     # ─────────────────────────────────────────
#     #  Alien Town Copy of Originial
#     # ─────────────────────────────────────────
#     label alien_town:
#         #Scene changes to the outskirts of the Alien Town.
#         scene bg AlienTown
#         with fade 

#         "The tablet's signal leads you to the outskirts of a small settlement—if it can even be called that anymore.
#         From a distance, the houses look almost cheerful, painted in bright colors that don't belong on Earth."

#         "But the closer you get, the more wrong everything feels."

#         "The air is warm. Too warm. And the wind is completely still."
#         "Your tracker vibrates once."

#         "{b}ALPHA-TEAM SIGNALS DETECTED — MULTIPLE SOURCES{/b}"

#         "{b}All{/b} of them are somewhere inside the cornfield ahead. You tighten your grip on your rifle and step forward."

#         # Change scene to cornfield
#         # Not sure if there is supposed to be ambient sounds of birds and insects. Describing the sounds seems weird
#         "The corn towers over you—far taller than it should be. The stalks sway gently, even though there's no breeze."
#         "The stalks brush against your armor with a soft, rubbery texture. Not like plants. More like skin."

#         "Your tracker pings again."
#         "{b}ALPHA-5 — LAST POSITION: 42m{/b}"
#         "You push deeper into the corn."

#         # Maybe another scene change for the rustling cornfield? Or audio?
#         "You take another step."
#         "Something takes one with you."
#         "You freeze."
#         "The cornfield freezes with you."
#         "Your tracker vibrates again—more urgently this time."
#         "{b}ALPHA-5 — LAST POSITION: 18m{/b}"
#         "You force yourself to keep moving."

#         # Tightening cornfield path. Really feels like this should be a new scene but idk.
#         "The deeper you go, the narrower the path becomes."
#         "You try to push them aside. They bend too easily—like muscle, not plant fiber."

#         "Your flashlight catches something on one of the stalks:"
#         # Maybe a scene change here to reveal the blood
#         "A smear of dried blood."
#         "Human...You swallow hard and continue."

#         # Scene changes and reveals a house
#         # "Up close, the walls pulse faintly, like they're breathing." -Not sure how pulsing walls are gonna look
#         "Your tracker vibrates once."
#         "{b}ALPHA-5 — LAST POSITION: 3m{/b}"

#         mc "This is the place."
#         # Scene changes to the inside of the house I guess?
#         "You step inside"
#         "The air is warm and humid. The walls bulge slightly, as if something beneath them shifts when you're not looking." #Again, not sure if animiated background is possible
#         "Your flashlight beam catches something on the floor:"
#         "A rifle. A torn glove. A smear of blood leading toward a back room." # This could be edited to be interactible I think, but I can't implement this right now.

#         "You follow the blood trail."

#         #Scene change again:
#         "The room is empty—except for a single boot lying in the center of the floor. The floor beneath it bulges upward in a human-shaped outline, frozen mid-struggle."
#         #"The walls around the outline are stretched, as if something inside them pushed outward before being pulled back in."
#         #"A sidearm lies nearby, bent at an impossible angle."
#         #The above 2 lines feel weird to narrate. IDK if it'll be possible to explain this just visually. Or if Jordan will have time.
#         "This is where Alpha-5 died."

#         "Your tracker pings again—another signal deeper in the town."
#         "You leave quickly"

#         # The cornfield comes back, and then transitions to revealing an identical house, just different colors to the previous one
#         "Your tracker vibrates violently."
#         "{b}ALPHA-7 — LAST POSITION: 0m{/b}"
#         # Another interior. Recolor previous ones I guess?
#         "You step inside."
#         "{b}*BAM!!!*{/B}" #Or use audio
#         "The door slams shut behind you."
#         # "The walls ripple." Probably not possible to show.

#         "Something moves under the floorboards." #Add SFX
#         # "Your flashlight flickers, then stabilizes." This might be visually represented? Maybe
#         "On the floor lies a cracked helmet marked: {b}ALPHA-7{/b}"
#         "Next to it, half-melted into the fleshy floor, is a small recording device."
#         "You pry it free."
#         "It crackles to life."
        
#         #[BEGIN LOG]
#         a7 "…Alpha-7… recording. I don't know how long I've got. The others… they're gone. Not dead. Just… gone."
#         a7 "…we touched down near the town at dusk. Looked abandoned from a distance. Up close… The walls were warm. Like skin. It felt like the houses were listening to us breathe."
#         a7 "Alpha‑3 ordered recon. Standard sweep. We split up to check the structures. Empty rooms, empty streets… but the air felt thick. Like the whole damn place was holding its breath."
#         #[STATIC — LOW HUM]
#         a7 "…movement in the cornfield. Something tall. Kept pace with us but never stepped into the light. Every time I turned, it froze."
#         a7 "…first contact hit after nightfall. Fast. Invisible. Rounds didn't slow it. It didn't even try to kill us—just herded us deeper into the town like cattle."
#         a7 "…Alpha‑5 went into one of the houses. The door slammed behind him. When we forced it open… the room wasn't the same. Warmer. Breathing. No sign of him."
#         #[AUDIO DISTORTION — ORGANIC SHIFTING]
#         a7 "…that's when I saw it. The thing in the corn. Flesh‑colored. Limbs like stretched muscle. It moved like it was part of the town… or the town was part of it."
#         a7 "…it tore through the others. I ran. I don't know where they went. The houses shift when you're not looking. I swear I can hear them whispering under the floorboards."
#         a7 "…I'm inside now. Walls feel closer. Something's moving under the floor. I think it knows I'm here."
#         #[WEAPON CHAMBERING]
#         a7 "…if anyone finds this… don't stay here. Don't touch the walls. And whatever you do… don't let the thing in the cornfield see you. Keep moving and get the hell out."
#         #[UNINTELLIGIBLE ORGANIC SHIFTING — WET, LOW RUMBLE]
#         a7 "…it's at the door…"
#         # [GUNSHOTS — THEN SUDDEN SILENCE]
#         # [VOICE RETURNS — WRONG, MIMICKED, MULTIPLE LAYERS]
#         a7 "…if… you… out there… come… … your friends… are all… here…"
#         a7 "…it's… a… worse fate… to be hunted… by… me…"
#         # [STATIC — SIGNAL COLLAPSE]
#         # [END LOG]

#         #"You've recovered Alpha-7's log." #Can change how to represent this later.
#         "As you continue to explore the house, you find subtle signs of Alpha-3's struggle."

#         # Scene changes to show the backdoor.
#         # The rear doorframe is shattered outward.
#         # Deep gouges—human fingernails—run across the surface.
#         # Description of the door frame can just be visual

#         "A broken comms unit lies on the floor, still displaying:"
#         "{b}ALPHA-3 — SIGNAL LOST{/b}" #This could be visually displayed too...

#         # "The floor near the door is warped, as if something heavy dragged across it." (This could just be visually displayed. Or kept in text.)
#         "One section of wall is torn open from the inside. The edges pulse faintly, trying to close."
#         # Cut to a new background showing the soldier uniform in the wall
#         "Inside the tear, you see a scrap of fabric—Alpha‑3's uniform color."
#         "He tried to escape."
#         "He didn't make it."

#         "As you turn to leave, the house shifts."
#         #Change scene to creepy door
#         "Something opened the door as if expecting you to follow it."
#         #"Looking out the window, you notice it is going to be night soon as the streetlights light a pathway towards the church which is incredibly well lit." This can just be shown with lighting the in background

#         jump round_1