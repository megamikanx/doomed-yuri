label fungus_vday:
    scene bg_courtyard

    play sound "audio/main_event.ogg"
    
    show fungus neutral at center
    with dissolve

    fungus "my spots been taken💔"
    
    show fungus angry with dissolve
    fungus "everybody out here yappin about true love n shit..."
    fungus "brah watch those highlights be gone in a week."

    menu:
        "It's Valentines Day. I wanted to give you some chocolate.":
            $ fungus_affection += 3
            show fungus suprised with dissolve
            fungus "...?!"
            show fungus happy with dissolve
            fungus "aight twin maybe I was just salty."
            fungus "so...ya like jazz?"

            player_thoughts "I'm glad she likes it..."
            player_thoughts "I spent the entire day with Fungus-chan."

        "Sike.":
            show fungus angry with dissolve
            fungus "brah not u pissing me off too"
            fungus "gtfo"

            player_thoughts "What? I thought she'd be more in the spirit."

    return


