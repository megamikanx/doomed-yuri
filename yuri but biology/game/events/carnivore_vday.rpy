label carnivore_vday:
    scene bg_cafeteria

    play sound "audio/main_event.ogg"

    show carnivore smug with dissolve
    carnivore "“Well well… So you’re choosing to hang out with ME today."
    carnivore "Well, I guess I’ll allow it… hehe…"
    show carnivore angry with dissolve
    carnivore "Not that I want you here or anything!"
    show carnivore neutral with dissolve
    carnivore "Anyways for what reason did you come into my domain today?"
    show carnivore shy with dissolve
    carnivore "Better not be something stupid… like because today’s a certain day… or something...dumb like that."

    menu:
        "It's Valentines Day. I wanted to give you some chocolate.":
            $ carnivore_affection += 3
            show carnivore smug with dissolve
            carnivore "WHAT?! I totally knew that. What keen eyes you have!"
            show carnivore shy with dissolve
            carnivore "I meaaaan...I won't say no...we need to get our carbs in for the energy right?"

            player_thoughts "Phew...she seems to like it."
            player_thoughts "I spend the entire day with Carnivore-chan."

        "What day?":
            show carnivore angry with dissolve
            carnivore "...Yeah!"
            carnivore "Not like...all the konbinis are selling chocolate or anything..."
            carnivore "Hmph!"

            player_thoughts "What did I do this time..."

    return




