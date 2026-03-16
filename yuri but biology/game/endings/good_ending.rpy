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
    carnivore ""