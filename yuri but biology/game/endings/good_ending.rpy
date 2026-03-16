label good_ending:
    if trigger_good_ending:
        return

    $ trigger_good_ending = True

    scene bg_sunset

    player_thoughts "Ah, I've reached the end of my first week."
    player_thoughts "Maybe this school isn't so bad after all."

    show herbivore happy at center 
    with dissolve
    herbivore "[player-name]-kun! You made it through!"
    
    show herbivore shy at center
    with dissolve
    herbivore "There's a new salad bar that opened up down the street!"
    herbivore "We should totally go together..."

    show herbivore smug at center
    with dissolve
    herbivore "...and talk about important matters."

    hide herbivore smug

    show carnivore smug at center
    with dissolve
    carnivore "Ah, my underling! Not bad, you survived."

    show carnivore happy at center
    with dissolve 
    carnivore "I challenge you to a game of 1v1 basketball! Get ready to get smoked."

    hide carnivore happy

    show plant neutral at center
    with dissolve
    plant "[player_name]-kun (,; ⩌ ;,)"
    plant "I-I hope y-you had a great f-f-first w-week...!"
    show plant 4eyes shy at center
    with dissolve
    plant "I-if...you want to come over sometime..."
    plant "D-d-doors are always o-open...( ͡° ͜ʖ ͡° )" 

    hide plant 4eyes shy 

    show fungus neutral at center
    with dissolve
    fungus "gang we made it"
    
    show fungus happy at center
    with dissolve
    fungus "y'know what...I could give you my last cig..."
    fungus "if you really wanted."

    fungus "catch ya later n3rd🤓"

    hide fungus happy

    player_thoughts "Yeah...I think this is the start of a great school year."

    with dissolve

    return
