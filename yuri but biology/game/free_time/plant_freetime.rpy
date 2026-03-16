transform walk_forward_shake:
    xoffset 0
    yoffset 0
    linear 0.10 yoffset -4
    linear 0.10 yoffset 0
    linear 0.10 yoffset -4
    linear 0.10 yoffset 0
    linear 0.10 yoffset -4
    linear 0.10 yoffset 0

transform slight_surprise:
    yoffset 0
    ease 0.05 yoffset -10
    ease 0.08 yoffset 0

label free_plant_fungushere:
    scene bg_library

    "Both [plant] and [fungus] are here. Who do you want to talk to?"
    menu:
        "Both [plant] and [fungus] are here. Who do you want to talk to?{fast}"
        "[plant]":
            $ store.last_freetime_girl = "plant"
            $ freetime_index["plant"] += 1
            $ renpy.jump("free_plant"+ str(freetime_index["plant"] - 1))

        "[fungus]":
            $ meet_fungus = True
            $ store.last_freetime_girl = "fungus"
            $ freetime_index["fungus"] += 1
            $ renpy.jump("free_fungus"+str(freetime_index["fungus"] - 1))

    
    jump plan


label free_plant0:
    scene bg_library

    show plant surprise at center

    plant "{size=124}a-aah"
    if curr_timeslot_idx == 0:
        plant "{cps=15}G-G-Go{/cps}od Morning,{w=0.25} {cps=15}s-so{/cps}rry I didn’t see you there"
    else:
        plant "Hello {cps=10}s-so{/cps}rry I didn’t see you there"
    
    show plant neutral at center
    plant "Have you come to study too?"
    menu:
        plant "Have you come to study too?{fast}"

        "Yeah i’m looking for a book":
            show plant sad at center
            plant "{cps=7}o-o-o{/cps}h{w=1}, I hope you find it then..."
            hide plant sad with dissolve

        "Yeah can you help me with my work":
            if curr_timeslot_idx == 0:
                show plant shy at center
                plant "{cps=15}a-a-a{/cps}h, you {cps=5}c-can{/cps}{cps=30} sit here if you want...{/cps}"
                hide plant shy with dissolve
            else:
                show plant neutral at center
                plant "Sorry {w=0.25}, its not really a good time{w=0.25}, I'm really tired..."
                plant "I could help you another time though"
                hide plant neutral with dissolve
    
    jump plan

label free_plant1:
    scene bg_library

    if curr_timeslot_idx == 0:
        show plant neutral at center with dissolve
        plant "{cps=10}Rodents and{/cps}{w=0.25}{cps=3}... h{/cps}mm{cps=3}...{/cps}{w=0.1} {cps=30}Garden Bugs with...{w=0.25} no{cps=3}...{/cps}"
        menu:
            plant "Rodents and... hmm... Garden Bugs with... no...{fast}"

            "There's a book on leaf eaters over there":
                show plant sad at center
                plant "That's not what I was looking for..."
                hide plant sad with dissolve

            "There’s a book on flying bugs over there":
                show plant shy at center
                plant "{cps=15}T-Th{/cps}anks [player]-kun, {cps=3}...{/cps}{w=0.1} do you want t-to read it together?"
                hide plant shy with dissolve

    else:
        show plant neutral at center with dissolve
        plant "{cps=3}{size=124}Z{size=100}Zzz{size=64}zzz...{/cps}"
        hide plant neutral with dissolve
    jump plan

label free_plant2:
    scene bg_library

    if curr_timeslot_idx == 0:
        show plant neutral at center with dissolve
        plant "*sleeping quietly in sun rays*"
        menu:
            plant "*sleeping quietly in sun rays*{fast}"

            "*put blank over her*":
                show plant sad at center
                plant "{cps=5}hmm...{/cps} [player]-kun… what are you doing?{w=0.2} why did you wake me?"
                hide plant sad with dissolve

            "*open curtain more*":
                show plant happy at center
                plant "{cps=3}{size=124}Z{size=100}Zzz{size=64}zzz...{/cps}"
                hide plant happy with dissolve

    else:
        "{w=1}No ones here{cps=3}...{/cps}"
    jump plan

label free_plant3:
    scene bg_library

    show plant neutral with dissolve
    plant "..."
    player_thoughts "Ah, I wonder what she's reading."
    player_thoughts "I don't think she can hear me...let me just take a peak."

    show layer master at walk_forward_shake
    $ renpy.pause(0.8)

    show layer master

    player_thoughts "What's the title..."
    player_thoughts "The 12-Tentacled Kraken and Bang Bang Paradise...?"

    menu:
        "Whatcha got there?":
            show plant shy at center, slight_surprise 
            plant "{size=+12}[player_name]-kun?!?!!"
            plant "I...I didn't think you're in the library at this time..."
            show plant megablush with dissolve
            plant "U-uhm...don't worry about it!"
            player_thoughts "Should I have not looked...?"
        
        "I like the part where he grows another tentacle.":
            $ plant_affection += 1
            show plant shy with dissolve
            plant "[player_name]-kun?!"

            show plant megablush with dissolve
            plant "I didn't know you were into the Bang Bang Paradise series..."
            plant "Th-this is the newest one! The main character is so slimy...my favorite trope."

            show plant shy with dissolve
            plant "W-w-we should talk about it in depth s-sometime...!"

            player_thoughts "It used to be my favorite series in middle schoool...didn't know people still read the manga."

    jump plan



