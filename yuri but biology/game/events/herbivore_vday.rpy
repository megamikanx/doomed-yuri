label herbivore_vday:
    scene bg_classroom

    play sound "audio/main_event.ogg"


    show herbivore neutral with dissolve
    herbivore "Oh, [player_name]-kun!"
    herbivore "What brings you here? I thought everybody was exchanging chocolates on the courtyard."

    show herbivore shy with dissolve
    herbivore "Unless..."

    menu:
        "It's Valentines Day. I wanted to give you some chocolate.":
            $ herbivore_affection += 3
            show herbivore happy with dissolve

            herbivore "Oh my god, candy hearts!"
            herbivore "I'll keep this close to my heart...in my second stomach!"

            show herbivore neutral with dissolve

            herbivore "Oh..and what do they say?"
            herbivore "Fuck...meat eaters...?"

            show herbivore smug with dissolve
            herbivore "You've got good taste in candy."
            
            player_thoughts "Phew...she seems to like it."
            player_thoughts "I spend the entire day with Herbivore-chan."
        
        "Keep yo racist ahh away from meh.":
            show herbivore smug with dissolve
            
            herbivore "Chud."

            player_thoughts "Someone needs to clock her..."

    $store.curr_timeslot_idx = 6
    jump plan
    return
