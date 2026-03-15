



label intro:

    #exposition dump at start of game
    player "blah balh"



label name_loop:

    $ player_name = renpy.input("Whats your name:")

    $ player = Character("[player_name]", kind=base_char)

    menu:
        player "Is this my name"

        "Yes":
            herbivore "Nice to meet you [player]-kun"

        "No":
            jump name_loop

    return

    
