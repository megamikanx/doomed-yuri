label plant_vday:
    scene bg_library

    play sound "audio/main_event.ogg"

    show plant neutral at center
    with dissolve

    plant "H-hey (name)-kun… How c-come you’re here?"
    plant "S-surely...y-you know what day today is right… (,,>﹏<,,)"

    menu:
        "It's Valentines Day, isn't it? I wanted to give you some chocolate.":
            $ plant_affection += 3
            show plant suprised with dissolve
            plant "W-woah! I didn't expect you to actually have brought some..."
            show plant happy with dissolve
            plant "Ureshii desu ><"
            plant "I'll be sure to repay the favor..."
            
            player_thoughts "I'm glad she likes it..."
            player_thoughts "I spent the entire day with Plant-chan."

        "Today? Isn't it a Thursday?":
            show plant sad with dissolve
            plant "T-todays...not even a Thursday..."
            plant "I guess he doesn't care..."

            player_thoughts "What? Did I forget to cross Thursday off my calendar..."

    return