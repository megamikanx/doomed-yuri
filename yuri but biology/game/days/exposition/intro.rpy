



label intro:

    scene courtyard_bg
    #exposition dump at start of game
    player "It’s my first day at eco-gakuen, this supposedly great school accepting all kinds of different students." 
    player "I had to transfer out of my old school because someone brought in an animal infected with some kind of unknown disease." 
    player "It happened right before an exam I was about to take that I crammed for..."
    player "What a waste of studying amirite."
    player "Anyways the school closed down because most of the staff and students caught the infection and died. And now the school is permanently enclosed by a 20 mile quarantine area." 
    player "So now I’m here I guess. I hear there are some pretty weird people going to eco-gakuen."
    player "Let’s hope that isn’t true…" 
    player "Well here goes. "

    "*opens door*"

    scene classroom_bg

    herbivore "Oh"
    herbivore "You must be the transfer student!"
    herbivore "Weird.. you look awfully normal."
    herbivore "Anyways, I’m Herbivore chan, the class president."
    herbivore "What's your name?"


label name_loop:

    $ player_name = renpy.input("Whats your name:")

    $ player = Character("[player_name]", kind=base_char)

    menu:
        player "Is this my name"

        "Yes":
            herbivore "Nice to meet you [player]-kun"

        "No":
            jump name_loop

    herbivore "Have a seat wherever, {w} I’ll introduce you to your class-"
    return

    
